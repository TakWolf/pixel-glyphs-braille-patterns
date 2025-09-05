# 像素字形 - 盲文图案

[![License OFL](https://img.shields.io/badge/license-OFL--1.1-orange)](LICENSE-OFL)
[![License MIT](https://img.shields.io/badge/license-MIT-green)](LICENSE-MIT)
[![Releases](https://img.shields.io/github/v/release/TakWolf/pixel-glyphs-braille-patterns)](https://github.com/TakWolf/pixel-glyphs-braille-patterns/releases)

`2800 ~ 28FF; Braille Patterns`

## 原理

一个盲文图案由最多 8 个点组成，共 256 种图案。其变化规律满足二进制规则。因此，按顺序点亮对应的点即可生成全部字形。

需要注意的是，历史上盲文仅使用 6 个点，底部两个点是后来添加的。因此，底部两个点顺序和上面 6 个点顺序不同。

8 个点的顺序如下：

```text
┌─────┐
│ 1 4 │
│ 2 5 │
│ 3 6 │
│ 7 8 │
└─────┘
```

## 程序依赖

- [Pixel Font Knife](https://github.com/TakWolf/pixel-font-knife)
- [Loguru](https://github.com/Delgan/loguru)

## 许可证

分为「字形」和「程序」两个部分。

### 字形

使用 [「SIL 开放字体许可证第 1.1 版」](LICENSE-OFL) 授权。

### 程序

使用 [「MIT 许可证」](LICENSE-MIT) 授权。
