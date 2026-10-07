# Resource review

English | [简体中文](resource-review.md) · [Back to the list](../README.md)

Checked on October 7, 2026 (Beijing time). This update added eight projects and retained the existing entries.

## Selection

We checked relevance to Typora before comparing stars, archive status and commits over the past six months. For tools, we favored established projects with ongoing feature work or fixes. Themes have smaller audiences, so previews, installation instructions and recent changes also informed the choice. We did not lower the bar simply to add more entries.

Star counts come from the GitHub API. Dates show the latest commit's committer timestamp on the default branch, converted to Beijing time. Commit counts start on April 7, 2026 UTC and cover only the first page of 100 results; “≥100” means that limit was reached. Counts include merges, documentation and automated changes. They are not feature counts, release frequency or a compatibility guarantee.

## Added projects

| Project | Stars | Latest commit | Six-month commits | Reason for inclusion |
| --- | ---: | --- | ---: | --- |
| [mermaid-js/mermaid](https://github.com/mermaid-js/mermaid) | 90,569 | [ 2026-10-02 ](https://github.com/mermaid-js/mermaid/commits/develop/) | ≥100 | Used by Typora for built-in diagrams; no extra plugin is needed. |
| [jgm/pandoc](https://github.com/jgm/pandoc) | 46,594 | [ 2026-10-07 ](https://github.com/jgm/pandoc/commits/main/) | ≥100 | A direct dependency for some Typora import and export formats. |
| [Molunerfinn/PicGo](https://github.com/Molunerfinn/PicGo) | 27,315 | [ 2026-10-07 ](https://github.com/Molunerfinn/PicGo/commits/dev/) | 33 | Desktop image uploading, with official Typora integration instructions. |
| [Kuingsmile/PicList](https://github.com/Kuingsmile/PicList) | 3,770 | [ 2026-10-07 ](https://github.com/Kuingsmile/PicList/commits/dev/) | ≥100 | Remote image and file management, with recent features and fixes. |
| [gee1k/uPic](https://github.com/gee1k/uPic) | 3,718 | [ 2026-06-12 ](https://github.com/gee1k/uPic/commits/master/) | 2 | A native macOS uploader; included as a platform option despite fewer updates. |
| [PicGo/PicGo-Core](https://github.com/PicGo/PicGo-Core) | 991 | [ 2026-10-07 ](https://github.com/PicGo/PicGo-Core/commits/dev/) | 15 | Command-line uploading, distinct from the desktop app. |
| [lipengzhou/typora-theme-auto-numbering](https://github.com/lipengzhou/typora-theme-auto-numbering) | 286 | [ 2026-08-27 ](https://github.com/lipengzhou/typora-theme-auto-numbering/commits/master/) | 1 | Heading and TOC numbering; useful but not frequently updated. |
| [Muyiiiii/Typora_Claude-Like_Theme](https://github.com/Muyiiiii/Typora_Claude-Like_Theme) | 157 | [ 2026-07-03 ](https://github.com/Muyiiiii/Typora_Claude-Like_Theme/commits/master/) | 21 | Three color variants, installation instructions, author previews and recent theme fixes. |

None of these projects was archived when checked. Recent records for PicGo, PicList, PicGo-Core, Pandoc and Mermaid include features, refactoring or fixes. Claude-like includes fixes for dark mode and math display. uPic and the numbering styles have recent maintenance, but should not be described as frequently updated.

## Candidates not added

- [Ursine](https://github.com/noatpad/typora-theme-ursine): 740 stars; last repository push on December 9, 2022. Not selected in this round, which favored recent maintenance.
- [Typora Purple](https://github.com/hliu202/typora-purple-theme): 503 stars; last repository push on March 4, 2024. Not added this time.
- [Typora Gitbook](https://github.com/h16nning/typora-gitbook-theme): 316 stars; archived.
- [typora_claude](https://github.com/blaxisomu/typora_claude): 248 stars and 55 commits in the period, but its README had brief installation instructions and no preview images were found in the repository. We chose Claude-like for its fuller instructions and previews. These are separate projects.

“Last repository push” means GitHub's `pushed_at`, used for initial screening. It is not the same as the latest commit on the default branch and does not prove a project is abandoned. Existing entries such as Drake remain in the list despite less frequent updates.

## Sources for features and integration

- [Typora image upload guide](https://support.typora.io/Upload-Image/): integration with PicGo, PicGo-Core, PicList and uPic.
- [Typora Pandoc guide](https://support.typora.io/Install-and-Use-Pandoc/): import and export dependencies.
- [Typora diagram guide](https://support.typora.io/Draw-Diagrams-With-Markdown/): built-in Mermaid support.
- [Typora numbering guide](https://support.typora.io/Auto-Numbering/): CSS-based numbering.
- Each added project's README was also checked for features and installation information. The Claude-like preview uses the original image linked by its author; it returned HTTP 200 with an image/png content type when checked.

## Scope

This review checked public documentation, stars, commit records and the new theme's preview URL. It did not install or run these tools, or retest every existing entry. Counts and dates are a snapshot and may change.

## Existing entries reviewed

On 2026-10-07, we checked the public READMEs, installation requirements, archive status and licenses of the following projects. All six were unarchived; none was installation-tested.

| Project | Findings |
| --- | --- |
| [Typora plugin](https://github.com/obgnail/typora_plugin) | Native Windows/Linux support with Typora ≥0.9.98; no native macOS support. Added full-text search, tags and automatic numbering to the description. |
| [Typora Community Plugin](https://github.com/typora-community-plugin/typora-community-plugin) | Plugin management, command panel, tabs and split views; see upstream's compatibility table for versions on each desktop platform. |
| [Collapsible Section](https://github.com/typora-community-plugin/typora-plugin-collapsible-section) | Requires Community Plugin; folds headings, lists, code blocks and tables. |
| [Typora Copilot](https://github.com/Snowflyt/typora-copilot) | Upstream requires an active Copilot subscription; Typora 1.10 and later also require Node.js ≥20. |
| [VLOOK](https://github.com/MadMaxChow/VLOOK) | Themes and HTML export extensions; existing placement and description retained. |
| [Upgit](https://github.com/pluveto/upgit) | Supports Windows/Linux/macOS; requires destination configuration. The GitHub backend needs a repository and a token with contents read/write permissions. |

## Pending review

- [typora-plugin-bilibili](https://github.com/xlzy520/typora-plugin-bilibili): both the public project page and GitHub API returned 404 on retry on 2026-10-07. Moved here from the homepage recommendations. This does not distinguish deletion, private visibility or migration. Restore after finding an accessible original project or an author-confirmed replacement and reviewing its instructions.

## Theme images reviewed

Checked preview sources and repository licenses for all 14 themes; see [image source records](image-sources.md). Spring now shows a document preview, and Phycat uses an image in the author's current README. Vue's original author displays and credits the Vue Dark fork, so that preview is not a mismatch; the description now identifies the dark variant. Four images have unresolved usage terms; their entries retain project and author-preview links.

Theme installation, plugin behavior and export output were not tested. An unarchived theme is not a guarantee of compatibility with current Typora. Star and commit figures for the earlier eight additions remain dated snapshots above.
