from loguru import logger
from pixel_font_knife.mono_bitmap import MonoBitmap

from tools.configs import path_define


def _load_parts(font_size_x: int, font_size_y: int) -> dict[int, MonoBitmap]:
    parts = {}
    for i in range(1, 9):
        file_path = path_define.parts_dir.joinpath(f'{font_size_x}x{font_size_y}', f'{i}.png')
        bitmap = MonoBitmap.load_png(file_path)
        assert bitmap.width == font_size_x
        assert bitmap.height == font_size_y
        bitmap.save_png(file_path)
        parts[i] = bitmap
    return parts


def make_glyphs(font_size_x: int, font_size_y: int):
    outputs_dir = path_define.outputs_dir.joinpath(f'{font_size_x}x{font_size_y}', '2800-28FF Braille Patterns')
    outputs_dir.mkdir(parents=True, exist_ok=True)

    parts = _load_parts(font_size_x, font_size_y)
    canvas = MonoBitmap.create(font_size_x, font_size_y)
    for code_point in range(0x2800, 0x28FF + 1):
        bitmap = canvas
        bin_string = f'{code_point - 0x2800:08b}'
        for i, c in enumerate(reversed(bin_string)):
            if c == '0':
                continue
            bitmap = bitmap.plus(parts[i + 1])
        bitmap.save_png(outputs_dir.joinpath(f'{code_point:04X}.png'))
    logger.info('Make glyphs: {}x{}px', font_size_x, font_size_y)
