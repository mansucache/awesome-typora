import tempfile
import unittest
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from check_catalog import check, anchors, resource_ids


class CatalogChecks(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        (self.root / 'imgs').mkdir()
        (self.root / 'imgs/awesome-typora-banner.png').write_bytes(b'fixture')
        for name, other in [('README.md', 'README.zh-CN.md'), ('README.zh-CN.md', 'README.md')]:
            (self.root / name).write_text(
                f'[Language]({other})\n<img src="imgs/awesome-typora-banner.png" alt="Banner" />\n'
                '# Catalog\n[Project](https://example.org/project)\n', encoding='utf-8')

    def append(self, text):
        with (self.root / 'README.md').open('a', encoding='utf-8') as f:
            f.write(text)

    def test_valid_catalog(self):
        self.assertEqual(check(self.root), [])

    def test_missing_file_and_anchor(self):
        self.append('[Gone](missing.md)\n[Section](#gone)\n')
        errors = check(self.root)
        self.assertTrue(any('missing file' in e for e in errors))
        self.assertTrue(any('missing anchor' in e for e in errors))

    def test_language_drift(self):
        self.append('[Extra](https://example.org/extra)\n')
        self.assertTrue(any('differ' in e for e in check(self.root)))

    def test_broken_table_and_alt(self):
        self.append('| A | B |\n| --- | --- |\n| One |\n<img src="imgs/awesome-typora-banner.png" />\n')
        errors = check(self.root)
        self.assertTrue(any('table' in e for e in errors))
        self.assertTrue(any('alt text' in e for e in errors))

    def test_signed_url(self):
        self.append('[Temporary](https://example.org/image?jwt=example)\n')
        self.assertTrue(any('signed URL' in e for e in check(self.root)))

    def test_existing_but_different_local_image(self):
        (self.root / 'imgs/other.png').write_bytes(b'fixture')
        self.append('<img src="imgs/other.png" alt="Different" />\n')
        self.assertTrue(any('image sources differ' in e for e in check(self.root)))

    def test_language_switch_required(self):
        p = self.root / 'README.md'
        p.write_text(p.read_text().replace('[Language](README.zh-CN.md)', ''), encoding='utf-8')
        self.assertTrue(any('language switch' in e for e in check(self.root)))

    def test_code_examples_and_duplicate_anchors(self):
        self.append('```md\n[Example](does-not-exist.md)\n```\n')
        self.assertEqual(check(self.root), [])
        self.assertEqual(anchors('# A\n## A\n<a id="主题"></a>'), {'a', 'a-1', '主题'})

    def test_duplicate_in_both_editions(self):
        for name in ('README.md', 'README.zh-CN.md'):
            with (self.root / name).open('a', encoding='utf-8') as f:
                f.write('- [PicGo](https://github.com/Molunerfinn/PicGo)\n' * 2)
        self.assertTrue(any('duplicate resource' in e for e in check(self.root)))

    def test_navigation_and_description_references_allowed(self):
        self.append('[Navigation](https://example.org/project)\n')
        p = self.root / 'README.zh-CN.md'
        p.write_text(p.read_text() + '[导航](https://example.org/project)\n', encoding='utf-8')
        self.assertEqual(check(self.root), [])

    def test_repository_aliases_preserve_deep_links(self):
        ids = resource_ids('- [A](https://github.com/owner/project)\n'
                           '- [B](https://github.com/OWNER/project/blob/main/README.md)\n'
                           '- [C](https://github.com/owner/project/blob/main/docs/guide.md)\n')
        self.assertEqual(ids[0], ids[1])
        self.assertNotEqual(ids[0], ids[2])

    def test_missing_review_translation(self):
        (self.root / 'docs').mkdir()
        (self.root / 'docs/resource-review.md').write_text('# Review\n', encoding='utf-8')
        self.assertTrue(any('Both resource review editions' in e for e in check(self.root)))

    def test_review_facts(self):
        (self.root / 'docs').mkdir()
        row = '| [Tool](https://github.com/example/tool) | 1,234 | [2026-10-07](https://example.org/commits) | 12 | Description |\n'
        zh = self.root / 'docs/resource-review.md'
        en = self.root / 'docs/resource-review.en.md'
        zh.write_text(row.replace('Description', '说明'), encoding='utf-8')
        en.write_text(row, encoding='utf-8')
        self.assertEqual(check(self.root), [])
        for before, after in [('1,234', '1'), ('2026-10-07', '2026-10-06'), ('| 12 |', '| 1 |')]:
            en.write_text(row.replace(before, after), encoding='utf-8')
            self.assertTrue(any('review facts differ' in e for e in check(self.root)))


if __name__ == '__main__':
    unittest.main()
