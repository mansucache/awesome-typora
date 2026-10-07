# Contributing / 参与贡献

[English](#english) · [简体中文](#简体中文)

## English

Recommend a resource, report a broken link, or improve an entry through [Issues](https://github.com/mansucache/awesome-typora/issues). English and Chinese are both welcome; you do not need to prepare a translation to make a suggestion.

For a new resource, include its canonical project URL, what it adds to a Typora workflow, and any known platform or version requirements. For a theme, include an author-provided preview. Say whether you tried it yourself, and disclose if it is your project.

Include installation documentation and recent maintenance information if available. For themes with fewer stars or updates, explain their specific use. Avoid duplicate forks without a clear difference, unofficial activation tools and download mirrors of uncertain origin.

A single-language draft PR is welcome. Mark missing translations or checks under “Help needed”; a maintainer can help complete them before merging.

Before merging a pull request:

- Keep README.md (English) and README.zh-CN.md aligned: the same resources, order and preview images. Link to each project's English or Chinese documentation where available.
- Write a short, factual description. Do not claim an installation was tested unless it was.
- Use stable image URLs, not expiring signed links. Include descriptive alt text and keep the 280-pixel preview width. Credit the source; only copy images into this repository when their reuse terms allow it.
- Date any star counts or maintenance claims. Update both review documents when changing their findings; do not silently replace a historical snapshot with undated numbers.
- Check local links, section anchors, image URLs and Markdown tables in both editions.

For an unavailable resource, include the failing URL and what happened. A timeout or 403 response alone is not proof that the project is gone. Note redirects or archive status, and explain any proposed replacement or removal. Report bugs in a listed tool to its own project.

### Checks and discussion

Before merging, the contributor or maintainer runs `python3 scripts/check_catalog.py` and `python3 -m unittest discover -s tests -v`. See the [maintenance guide](docs/maintenance.md#english) for what these checks cover.

No harassment, discriminatory attacks, spam or disclosure of private information. Maintainers may remove abusive content or close off-topic threads. For sensitive reports, do not post private details in a public issue; use GitHub's built-in reporting tools where appropriate.

## 简体中文

欢迎通过 [Issues](https://github.com/mansucache/awesome-typora/issues) 推荐资源、报告失效链接或修正说明。中英文都可以，不需要先翻译才能提建议。

推荐资源时，请附上项目正式地址、它能为 Typora 用户解决什么问题，以及已知的平台或版本要求。主题请附作者提供的预览图。说明是否亲自使用过；如果是自己的项目，也请注明。

如已知，可附使用说明和近期维护情况。Star 较少或更新不频繁的主题，请说明具体用途。不收录没有明确差异的重复分支、非官方激活工具及来源不明的下载镜像。

可以先提交单语言草稿 PR，在“需要帮助”中注明待补翻译或检查，由维护者协助完成。

合并前：

- 同步 README.md（英文）和 README.zh-CN.md（中文）的资源、顺序与预览图。项目有对应语言文档时，可分别链接。
- 简短说明实际用途。没有安装测试过，就不要写成已经验证可用。
- 图片使用稳定地址，不使用带过期签名的临时链接。补上图片说明，预览宽度保持 280 像素。注明来源，只有在授权允许时才把图片复制进仓库。
- Star 和维护情况注明核验日期。修改核验结论时同步两份记录，不用未标日期的新数字覆盖历史快照。
- 检查两版的本地链接、章节跳转、图片地址和 Markdown 表格。

报告资源不可用时，请附出错地址和现象。超时或返回 403 不足以证明项目失效；如果发生跳转、归档，或建议替换、删除，请说明依据。具体工具的故障请到对应项目反馈。

### 检查与讨论

合并前由贡献者或维护者运行 `python3 scripts/check_catalog.py` 和 `python3 -m unittest discover -s tests -v`。检查范围见[维护手册](docs/maintenance.md#简体中文)。

请勿人身攻击、骚扰、歧视、刷屏或披露他人隐私。维护者可移除不当内容或关闭无关讨论；敏感举报不要在公开 Issue 中贴出私密细节，适用时使用 GitHub 自带的举报入口。
