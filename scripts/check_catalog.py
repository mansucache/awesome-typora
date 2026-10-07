"""Offline checks for this catalog's inline Markdown and HTML links (Python 3)."""

import re
import sys
from collections import Counter
from pathlib import Path
from urllib.parse import unquote, urlsplit


def prose(text):
    return re.sub(r"^(`{3,}|~{3,}).*?^\1\s*$", "", text,
                  flags=re.MULTILINE | re.DOTALL)


def links(text):
    pattern = r'\[[^\]\n]*\]\(([^)\s]+)\)|(?:href|src)="([^"]+)"'
    return [a or b for a, b in re.findall(pattern, prose(text))]


def anchors(text):
    text = prose(text)
    found = set(re.findall(r'<a\s+id="([^"]+)"', text))
    counts = {}
    for heading in re.findall(r'^#{1,6}\s+(.+?)\s*#*$', text, re.MULTILINE):
        slug = re.sub(r'[^\w\- ]', '', heading.lower()).replace(' ', '-')
        n = counts.get(slug, 0)
        found.add(slug if n == 0 else f'{slug}-{n}')
        counts[slug] = n + 1
    return found


def canonical(url):
    # Language-specific documentation for the same project is intentional.
    return url.replace('/BingyanStudio/LapisCV/blob/main/README-CN.md',
                       '/BingyanStudio/LapisCV')


def external_links(text):
    return [canonical(u) for u in links(text)
            if urlsplit(u).scheme in ('http', 'https')]


def resource_ids(text):
    """Only entry-leading links, not navigation or links in descriptions."""
    urls = re.findall(r'^(?:- |\| )\[[^\]]+\]\((https?://[^)]+)\)',
                      prose(text), re.MULTILINE)
    identities = []
    for url in urls:
        url = canonical(url)
        parsed = urlsplit(url)
        path = parsed.path.rstrip('/')
        # Treat repository README/tree entry points as the same project.
        if parsed.netloc.lower() == 'github.com':
            path = re.sub(r'/(?:tree/[^/]+|blob/[^/]+/README(?:[^/]*)?)$', '', path, flags=re.I).removesuffix('.git').lower()
        identities.append((parsed.netloc.lower(), path, parsed.query))
    return identities


def review_values(text):
    """Compare dated review table facts, leaving translated prose independent."""
    values = []
    for line in text.splitlines():
        cells = [cell.strip() for cell in line.strip('|').split('|')]
        if line.startswith('| [') and len(cells) == 5 and re.fullmatch(r'[\d,]+', cells[1]):
            date = re.search(r'\d{4}-\d{2}-\d{2}', cells[2])
            urls = links(cells[0])
            if not date or not urls:
                values.append(('invalid review row', line))
            else:
                values.append((canonical(urls[0]), cells[1].replace(',', ''),
                               date.group(), tuple(links(cells[2])), cells[3]))
    return values


def check(root):
    root = Path(root).resolve()
    errors = []
    files = list(root.glob('*.md'))
    for directory in ('docs', '.github'):
        files.extend((root / directory).rglob('*.md'))
    for path in sorted(files):
        text = path.read_text(encoding='utf-8')
        label = path.relative_to(root)
        for url in links(text):
            parsed = urlsplit(url)
            if parsed.scheme or parsed.netloc:
                if re.search(r'[?&](jwt|X-Amz-Signature)=', url, re.I):
                    errors.append(f'{label}: expiring signed URL')
                continue
            target = (path.parent / unquote(parsed.path)).resolve() if parsed.path else path
            if root != target and root not in target.parents:
                errors.append(f'{label}: link outside repository: {url}')
                continue
            if not target.is_file():
                errors.append(f'{label}: missing file: {url}')
            elif parsed.fragment and target.suffix == '.md':
                if unquote(parsed.fragment) not in anchors(target.read_text(encoding='utf-8')):
                    errors.append(f'{label}: missing anchor: {url}')
        width = None
        for line in prose(text).splitlines():
            if line.startswith('|'):
                cells = len(re.split(r'(?<!\\)\|', line))
                if width is not None and cells != width:
                    errors.append(f'{label}: inconsistent table columns')
                width = cells
            else:
                width = None
        for tag in re.findall(r'<img\b[^>]*>', text):
            if not re.search(r'alt="[^"]+"', tag):
                errors.append(f'{label}: image missing alt text')
    editions = [root / 'README.md', root / 'README.zh-CN.md']
    if not all(p.is_file() for p in editions):
        errors.append('Both README editions are required')
    else:
        en, zh = [p.read_text(encoding='utf-8') for p in editions]
        for path, text in zip(editions, (en, zh)):
            for identity, count in Counter(resource_ids(text)).items():
                if count > 1:
                    errors.append(f'{path.name}: duplicate resource: {identity[0]}{identity[1]}')
        if external_links(en) != external_links(zh):
            errors.append('README resource links/images differ in content or order')
        if re.findall(r'<img\b[^>]*src="([^"]+)"', en) != re.findall(r'<img\b[^>]*src="([^"]+)"', zh):
            errors.append('README image sources differ in content or order')
        for text, other in ((en, 'README.zh-CN.md'), (zh, 'README.md')):
            if other not in links(text):
                errors.append(f'Missing language switch to {other}')
        for text in (en, zh):
            if not any(u.startswith('imgs/awesome-typora-banner') for u in links(text)):
                errors.append('README banner missing')
    reviews = [root / 'docs/resource-review.md', root / 'docs/resource-review.en.md']
    if any(p.exists() for p in reviews):
        if not all(p.is_file() for p in reviews):
            errors.append('Both resource review editions are required')
        elif review_values(reviews[0].read_text(encoding='utf-8')) != review_values(reviews[1].read_text(encoding='utf-8')):
            errors.append('Bilingual review facts differ: project, stars, date, source or commit count')
    return errors


if __name__ == '__main__':
    problems = check(Path(__file__).resolve().parents[1])
    for problem in problems:
        print(f'ERROR: {problem}')
    if not problems:
        print('Catalog checks passed: local links, anchors, tables, images and bilingual parity.')
    sys.exit(bool(problems))
