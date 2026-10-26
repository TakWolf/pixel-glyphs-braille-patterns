# 像素字形 - 盲文图案

[![License OFL](https://img.shields.io/badge/license-OFL--1.1-orange?style=flat-square)](LICENSE-OFL)
[![License MIT](https://img.shields.io/badge/license-MIT-green?style=flat-square)](LICENSE-MIT)
[![Releases](https://img.shields.io/github/v/release/TakWolf/pixel-glyphs-braille-patterns?style=flat-square)](https://github.com/TakWolf/pixel-glyphs-braille-patterns/releases)

`2800..28FF; Braille Patterns`

## 原理

一个盲文图案包含 8 个点位，每个点位有凸起和空白两种状态，因此共有 2⁸ = 256 种组合，其中包括全空白图案。

传统六点盲文的点位按先左列、后右列的顺序编号。八点盲文保留原有编号，将左下方和右下方新增的两个点位分别编号为 7 和 8，排列如下：

```text
┌─────┐
│ 1 4 │
│ 2 5 │
│ 3 6 │
│ 7 8 │
└─────┘
```

在 Unicode 编码中，第 1～8 点依次对应一个 8 位二进制数从低到高的各位：值为 1 表示该点凸起，值为 0 表示该点空白。将这个数加上区块起始码位 `U+2800`，即可得到对应字符的码位。

因此，遍历 0～255，并根据各位的值绘制对应点位，即可生成全部字形。

## 程序依赖

- [Pixel Font Knife](https://github.com/TakWolf/pixel-font-knife)
- [Loguru](https://github.com/Delgan/loguru)

## 许可证

分为「字形」和「程序」两个部分。

### 字形

采用 [SIL Open Font License version 1.1](LICENSE-OFL) 授权。

### 程序

采用 [MIT License](LICENSE-MIT) 授权。
