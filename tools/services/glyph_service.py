from loguru import logger
from pixel_font_knife.mono_bitmap import MonoBitmap

from tools.configs import path_define, FontSize


def _load_parts(font_size: FontSize) -> dict[int, MonoBitmap]:
    parts = {}
    for i in range(1, 9):
        file_path = path_define.parts_dir.joinpath(str(font_size), f'{i}.png')
        bitmap = MonoBitmap.load_png(file_path)
        assert bitmap.width == font_size // 2
        assert bitmap.height == font_size
        bitmap.save_png(file_path)
        parts[i] = bitmap
    return parts


def make_glyphs(font_size: FontSize):
    outputs_dir = path_define.outputs_dir.joinpath(str(font_size), '2800-28FF Braille Patterns')
    outputs_dir.mkdir(parents=True, exist_ok=True)

    parts = _load_parts(font_size)
    canvas = MonoBitmap.create(font_size // 2, font_size)
    for code_point in range(0x2800, 0x28FF + 1):
        bitmap = canvas
        bin_string = f'{code_point - 0x2800:08b}'
        for i, c in enumerate(reversed(bin_string)):
            if c == '0':
                continue
            bitmap = bitmap.plus(parts[i + 1])
        bitmap.save_png(outputs_dir.joinpath(f'{code_point:04X}.png'))
    logger.info('Make glyphs: {}px', font_size)
