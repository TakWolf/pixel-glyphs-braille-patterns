import logging

from scripts.configs import path_define
from scripts.utils import bitmap_util

logger = logging.getLogger(__name__)


def load_fragments(font_size: int) -> dict[int, list[list[int]]]:
    fragments = {}
    for i in range(1, 9):
        file_path = path_define.fragments_dir.joinpath(str(font_size), f'{i}.png')
        bitmap, width, height = bitmap_util.load_png(file_path)
        assert width == font_size // 2
        assert height == font_size
        bitmap_util.save_png(bitmap, file_path)
        fragments[i] = bitmap
    return fragments


def make_patterns(font_size: int, fragments: dict[int, list[list[int]]]):
    outputs_dir = path_define.outputs_dir.joinpath(str(font_size), '2800-28FF Braille Patterns')
    outputs_dir.mkdir(parents=True, exist_ok=True)

    for code_point in range(0x2800, 0x28FF + 1):
        bitmap = [[0] * (font_size // 2) for _ in range(font_size)]
        bin_string = f'{code_point - 0x2800:08b}'
        for i, c in enumerate(reversed(bin_string)):
            if c == '0':
                continue
            fragment = fragments[i + 1]
            for y, fragment_row in enumerate(fragment):
                for x, alpha in enumerate(fragment_row):
                    if alpha == 0:
                        continue
                    bitmap[y][x] = 1
        file_path = outputs_dir.joinpath(f'{code_point:04X}.png')
        bitmap_util.save_png(bitmap, file_path)
        logger.info("Make pattern: '%s'", file_path)
