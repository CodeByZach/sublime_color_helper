# ColorHelper
[![Latest Release][release-image]][release-link]
[![Build][github-ci-image]][github-ci-link]
[![Package Control Downloads][pc-image]][pc-link]
[![License][license-image]][license-link]

ColorHelper makes work with colors easier by providing inline color previews in your documents (ST3 build 3118+) and offers tooltips with color previews of stylesheet colors, provides color translation, and allows the storing and accessing of favorite colors in color palettes.  Most features are optionally configurable. For the most part, these tooltips should show any time the cursor is in a CSS, SCSS, or SASS color.  It should also appear when in HTML style attributes.

![Screenshot1](docs/src/markdown/images/composite.png)

![Screenshot2](docs/src/markdown/images/color_picker.png)

![Screencap3](docs/src/markdown/images/inline_preview.gif)

# Features

- Inline color previews.
- Useful tooltip popups that show the previews of selected colors.
- Support colors in CSS, SCSS, SASS, and HTML attributes.
- Show all the colors in a file in a special color palette in the tooltip.
- Allow saving, accessing, and managing colors in named color palettes all from the tooltip.
- Select and insert colors from the color palettes via the tooltip.
- Translate an existing color form to a new form the tooltip.  Supports `rgb`, `rgba`, `hex`, `hexa`, `hsl`, `hsla`, `gray`, `hwb`, and color names.
- Can optionally treat `hexa` format (`#RRGGBBAA`) as `#AARRGGBB`.

# Documentation

https://codebyzach.github.io/sublime_color_helper/

# License

ColorHelper is released under the MIT license.

[release-image]: https://img.shields.io/github/tag/CodeByZach/sublime_trailing_spaces.svg?label=version
[release-link]: https://github.com/CodeByZach/sublime_trailing_spaces/releases
[github-ci-image]: https://github.com/CodeByZach/sublime_trailing_spaces/workflows/build/badge.svg?branch=master&event=push
[github-ci-link]: https://github.com/CodeByZach/sublime_trailing_spaces/actions?query=workflow%3Abuild+branch%3Amaster
[pc-image]: https://img.shields.io/packagecontrol/dt/ColorHelper.svg?labelColor=333333&logo=sublime%20text
[pc-link]: https://packagecontrol.io/packages/ColorHelper
[license-image]: https://img.shields.io/badge/license-MIT-blue.svg?labelColor=333333
[license-link]: LICENSE
