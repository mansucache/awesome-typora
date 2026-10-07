# 资源核验记录

[English](resource-review.en.md) | 简体中文 · [返回清单](../README.zh-CN.md)

核验日期：2026-10-07（北京时间）。本次补充 8 个项目，原有资源保留。

## 筛选方式

先确认与 Typora 的关系，再比较 Star、归档状态和最近半年的提交记录。工具优先选择用户积累较多、仍有功能或修复提交的项目；主题的规模通常小得多，结合预览、安装说明和近期改动判断。没有为凑数量统一降低标准。

下表的 Star 来自 GitHub API，日期为默认分支最近一次提交的提交者时间，已转换为北京时间。提交数量从 2026-04-07 UTC 起统计，只读取第一页 100 条，达到上限时记为“≥100”；包含合并、文档和自动化提交，不能当作功能更新次数。它也不是发布频率或兼容性保证。

## 新增项目

| 项目 | Star | 最近提交 | 近半年提交 | 收录原因 |
| --- | ---: | --- | ---: | --- |
| [mermaid-js/mermaid](https://github.com/mermaid-js/mermaid) | 90,569 | [ 2026-10-02 ](https://github.com/mermaid-js/mermaid/commits/develop/) | ≥100 | Typora 内置图表功能使用的项目，不是额外安装的插件。 |
| [jgm/pandoc](https://github.com/jgm/pandoc) | 46,594 | [ 2026-10-07 ](https://github.com/jgm/pandoc/commits/main/) | ≥100 | Typora 部分导入导出功能直接依赖的工具。 |
| [Molunerfinn/PicGo](https://github.com/Molunerfinn/PicGo) | 27,315 | [ 2026-10-07 ](https://github.com/Molunerfinn/PicGo/commits/dev/) | 33 | 图片上传的桌面入口，Typora 官方文档有接入说明。 |
| [Kuingsmile/PicList](https://github.com/Kuingsmile/PicList) | 3,770 | [ 2026-10-07 ](https://github.com/Kuingsmile/PicList/commits/dev/) | ≥100 | 补充远端图片与文件管理，近期仍有功能与修复提交。 |
| [gee1k/uPic](https://github.com/gee1k/uPic) | 3,718 | [ 2026-06-12 ](https://github.com/gee1k/uPic/commits/master/) | 2 | macOS 原生上传工具；更新较少，作为平台选项保留。 |
| [PicGo/PicGo-Core](https://github.com/PicGo/PicGo-Core) | 991 | [ 2026-10-07 ](https://github.com/PicGo/PicGo-Core/commits/dev/) | 15 | 命令行上传方案，与桌面版用途不同。 |
| [lipengzhou/typora-theme-auto-numbering](https://github.com/lipengzhou/typora-theme-auto-numbering) | 286 | [ 2026-08-27 ](https://github.com/lipengzhou/typora-theme-auto-numbering/commits/master/) | 1 | 补充标题与目录编号；更新较少，不列为高频维护项目。 |
| [Muyiiiii/Typora_Claude-Like_Theme](https://github.com/Muyiiiii/Typora_Claude-Like_Theme) | 157 | [ 2026-07-03 ](https://github.com/Muyiiiii/Typora_Claude-Like_Theme/commits/master/) | 21 | 有三套配色、安装说明和作者预览图；近半年有主题修复提交。 |

以上项目核验时均未归档。PicGo、PicList、PicGo-Core、Pandoc 和 Mermaid 的近期记录包含功能开发、重构或修复；Claude-like 主题有深色模式与公式显示等修复。uPic 和自动编号样式只算近期有维护，不称为更新频繁。

## 没有新增的候选

- [Ursine](https://github.com/noatpad/typora-theme-ursine)：740 Star，仓库最后推送于 2022-12-09，不符合本次优先选择近期维护项目的方向。
- [Typora Purple](https://github.com/hliu202/typora-purple-theme)：503 Star，仓库最后推送于 2024-03-04，暂不补入。
- [Typora Gitbook](https://github.com/h16nning/typora-gitbook-theme)：316 Star，已归档。
- [typora_claude](https://github.com/blaxisomu/typora_claude)：248 Star，近半年有 55 次提交，但 README 安装说明较简略，仓库未找到预览图片；本次选择了说明和预览更完整的 Claude-like。两者是不同项目。

这里的“最后推送”是 GitHub 的 `pushed_at`，只用于初筛，不等同于默认分支最近提交，也不代表已经停止维护。旧清单中的 Drake 等主题仍保留，不因为更新较少就删除。

## 功能与接入来源

- [Typora 图片上传文档](https://support.typora.io/Upload-Image/)：确认 PicGo、PicGo-Core、PicList、uPic 与 Typora 的接入关系。
- [Typora Pandoc 文档](https://support.typora.io/Install-and-Use-Pandoc/)：确认导入导出依赖。
- [Typora 图表文档](https://support.typora.io/Draw-Diagrams-With-Markdown/)：确认 Mermaid 为内置支持。
- [Typora 自动编号文档](https://support.typora.io/Auto-Numbering/)：确认 CSS 编号方式。
- 新增项目的用途与安装信息同时对照各自 README。Claude-like 预览使用作者 README 中的原图，核验时返回 HTTP 200、image/png。

## 验证范围

本次完成公开资料、Star、提交记录与新增主题图片地址的核验，没有安装运行这些工具，也没有逐项复测旧资源。Star 和日期是上述日期的快照，后续可能变化。

## 旧条目复核

2026-10-07 复核了以下项目的公开 README、安装要求、归档状态和许可。以下六个项目当日均未归档；未进行安装实测。

| 项目 | 核对结果 |
| --- | --- |
| [Typora plugin](https://github.com/obgnail/typora_plugin) | 原生支持 Windows/Linux、Typora ≥0.9.98；macOS 不在原生支持范围。补充全文搜索、标签和自动编号用途。 |
| [Typora Community Plugin](https://github.com/typora-community-plugin/typora-community-plugin) | 提供插件管理、命令面板、标签页和分屏；三个桌面平台的版本范围见原项目兼容表。 |
| [Collapsible Section](https://github.com/typora-community-plugin/typora-plugin-collapsible-section) | 依赖 Community Plugin；支持折叠标题、列表、代码块和表格。 |
| [Typora Copilot](https://github.com/Snowflyt/typora-copilot) | 上游要求有效 Copilot 订阅；Typora 1.10 及以上还需 Node.js ≥20。 |
| [VLOOK](https://github.com/MadMaxChow/VLOOK) | 主题与 HTML 导出扩展，保留现有分类和用途说明。 |
| [Upgit](https://github.com/pluveto/upgit) | 支持 Windows/Linux/macOS；需配置上传目标，GitHub 后端需要仓库与具有内容读写权限的令牌。 |

## 待复核

- [typora-plugin-bilibili](https://github.com/xlzy520/typora-plugin-bilibili)：2026-10-07 重试公开项目页和 GitHub API，均返回 404。已从首页推荐区移到此处；无法据此区分删除、转为私有或迁移。找到可访问的原项目或作者确认的迁移地址，并复核说明后再恢复。

## 主题图片复核

检查了 14 个主题的预览来源和仓库许可，详情见[图片来源记录](image-sources.md)。Spring 改用实际文档预览，Phycat 改用作者当前 README 的图片。Vue 原作者明确展示并致谢 Vue Dark 分支，因此不能把该预览判为错配；条目已写明深色变体。四项图片的使用条款仍待确认，首页保留原有图片和作者项目链接，具体情况见图片来源记录。

本轮未实测主题安装、插件运行和导出效果；主题仓库未归档也不等于兼容当前 Typora。此前八个新增项目的 Star 和提交数据仍为上方注明日期的快照。
