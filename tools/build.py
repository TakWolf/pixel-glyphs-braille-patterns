import shutil

from tools.config import paths, options
from tools.services import glyph_service, publish_service


def main() -> None:
    if paths.BUILD_DIR.exists():
        shutil.rmtree(paths.BUILD_DIR)

    for glyph_width, glyph_height in options.GLYPH_SIZES:
        glyph_service.make_glyphs(glyph_width, glyph_height)
        publish_service.make_release_zip(glyph_width, glyph_height)


if __name__ == '__main__':
    main()
