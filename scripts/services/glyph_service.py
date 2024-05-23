import logging
import os.path

from scripts.configs import path_define
from scripts.utils import bitmap_util

logger = logging.getLogger('glyph_service')


def load_fragments(font_size: int) -> dict[int, list[list[int]]]:
    fragments = {}
    for i in range(1, 9):
        file_path = os.path.join(path_define.fragments_dir, str(font_size), f'{i}.png')
        data, width, height = bitmap_util.load_png(file_path)
        assert width == font_size // 2
        assert height == font_size
        bitmap_util.save_png(data, file_path)
        fragments[i] = data
    return fragments


def make_patterns(font_size: int, fragments: dict[int, list[list[int]]]):
    outputs_dir = os.path.join(path_define.outputs_dir, str(font_size), '2800-28FF Braille Patterns')
    os.makedirs(outputs_dir, exist_ok=True)

    for code_point in range(0x2800, 0x28FF + 1):
        data = [[0] * (font_size // 2) for _ in range(font_size)]
        bin_string = f'{code_point - 0x2800:08b}'
        for i, c in enumerate(reversed(bin_string)):
            if c == '0':
                continue
            fragment = fragments[i + 1]
            for y, fragment_row in enumerate(fragment):
                for x, alpha in enumerate(fragment_row):
                    if alpha == 0:
                        continue
                    data[y][x] = 1
        file_path = os.path.join(outputs_dir, f'{code_point:04X}.png')
        bitmap_util.save_png(data, file_path)
        logger.info("Make pattern file: '%s'", file_path)
