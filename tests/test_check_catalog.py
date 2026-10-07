import tempfile
import unittest
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from check_catalog import check, anchors


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


if __name__ == '__main__':
    unittest.main()
