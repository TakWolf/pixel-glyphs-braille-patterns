from typing import Literal, get_args

version = '0.1.0'

type FontSize = Literal[8, 10, 12, 14, 16]
font_sizes = list[FontSize](get_args(FontSize.__value__))
