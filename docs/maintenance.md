# Maintaining the catalog / 维护清单

[English](#english) · [简体中文](#简体中文)

## English

### Scope

Include themes, plugins, templates and tools used with Typora. General Markdown resources go in [Awesome Markdown](https://github.com/mansucache/awesome-markdown).

Keep previews and descriptions in the READMEs, and dated findings in the review documents. This is an independent community list. Listed projects and images retain their original licenses; inclusion does not certify safety or compatibility.

### Review steps

1. Check the original project's instructions, license, supported platforms, archive status and recent changes.
2. Compare it with existing entries. Describe what it adds. For themes, use an author-provided preview with a stable URL and record its source and terms in [image sources](image-sources.md); use an author-page link when terms are unclear.
3. Update both READMEs. Record the date and sources for star counts and maintenance findings in both review documents. Mark anything untested or unconfirmed.
4. Run the checks and preview both READMEs. Check the banner, theme table and language links before merging.

### Checks

Run from the repository root with Python 3:

```sh
python3 scripts/check_catalog.py
python3 -m unittest discover -s tests -v
```

The script uses the Python standard library to check:

- Local files and section links.
- Table columns and HTML image descriptions.
- Expiring signed image URLs.
- Matching resource links and images in both READMEs.
- Duplicate catalog entries and matching dated review figures in both languages.

It handles the inline Markdown and HTML links used here. External availability, page layout, translation, upstream licenses and tool behavior require manual review.

Once published, the workflow runs on pull requests, pushes to main and manual dispatch. It has read-only permissions, makes no external document uploads, and has no scheduled runs or automatic issue creation.

### Unavailable resources

Retry failed URLs and check the project page. A timeout or 403 alone does not establish that a resource is gone. If failures persist, mark the entry as unconfirmed and add the check date. Explain replacements and removals in the PR.

### Pending review

The older plugins and Upgit were reviewed on 2026-10-07. Track the unavailable Bilibili uploader in [pending reviews](resource-review.en.md#pending-review), and unresolved image terms in [image sources](image-sources.md). Installation and export tests remain outstanding.

## 简体中文

### 收录范围

收录供 Typora 使用的主题、插件、模板和工具。通用 Markdown 资源放在 [Awesome Markdown](https://github.com/mansucache/awesome-markdown)。

README 放预览图和简介，核验记录保存日期与依据。本项目为独立社区清单；收录项目和图片沿用各自许可，收录不代表安全或兼容性认证。

### 审核步骤

1. 查看原项目的安装说明、许可、支持平台、归档状态和近期改动。
2. 与现有条目比较，说明新增用途。主题预览使用稳定地址，在[图片来源](image-sources.md)记录出处与条款；条款不明时使用作者页面链接。
3. 同步两版 README。Star 和维护情况在两份核验记录中注明日期与来源，未实测或待确认的内容保留标注。
4. 运行检查，再预览两版首页。合并前确认横幅、主题表格和语言链接正常。

### 检查

在仓库根目录用 Python 3 运行上面的两条命令。脚本只依赖标准库，检查：

- 本地文件和章节链接。
- 表格列数与 HTML 图片说明。
- 带过期签名的图片地址。
- 两版 README 的资源链接和图片是否一致。
- 重复收录，以及两版核验表的 Star、日期、来源和提交数量是否一致。

脚本处理本仓库使用的行内 Markdown 和 HTML 链接。外链可用性、版面、翻译、上游许可和工具运行情况需人工核对。

工作流发布后，在 PR、main 推送和手动触发时运行。权限只读，不向外部上传文档，未设置定时运行或自动创建 Issue。

### 失效资源

链接访问失败时，先重试并查看项目主页。超时或 403 不能单独作为失效依据。反复失败的条目标注待确认状态和检查日期；替换或删除时，在 PR 中说明原因。

### 待核验

旧插件与 Upgit 已于 2026-10-07 复核公开说明。哔哩哔哩上传工具见[待复核记录](resource-review.md#待复核)，图片条款待确认项见[图片来源](image-sources.md)。安装和导出效果尚未实测。
