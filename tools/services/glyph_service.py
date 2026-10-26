from loguru import logger
from pixel_font_knife.bitmap.mono_bitmap import MonoBitmap

from tools.config import path_define


def _load_parts(glyph_width: int, glyph_height: int) -> dict[int, MonoBitmap]:
    parts = {}
    for i in range(1, 9):
        file_path = path_define.PARTS_DIR.joinpath(f'{glyph_width}x{glyph_height}', f'{i}.png')
        bitmap = MonoBitmap.load_png(file_path)
        assert bitmap.width == glyph_width
        assert bitmap.height == glyph_height
        parts[i] = bitmap
    return parts


def make_glyphs(glyph_width: int, glyph_height: int) -> None:
    outputs_dir = path_define.OUTPUTS_DIR.joinpath(f'{glyph_width}x{glyph_height}', '2800-28FF Braille Patterns')
    outputs_dir.mkdir(parents=True, exist_ok=True)

    parts = _load_parts(glyph_width, glyph_height)
    canvas = MonoBitmap.blank(glyph_width, glyph_height)
    for code_point in range(0x2800, 0x28FF + 1):
        bitmap = canvas
        bin_string = f'{code_point - 0x2800:08b}'
        for i, c in enumerate(reversed(bin_string)):
            if c == '0':
                continue
            bitmap = bitmap.union(parts[i + 1])
        bitmap.save_png(outputs_dir.joinpath(f'{code_point:04X}.png'))
    logger.info('Make glyphs: {}x{}px', glyph_width, glyph_height)
