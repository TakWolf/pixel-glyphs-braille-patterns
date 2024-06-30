from tools import configs
from tools.configs import path_define
from tools.services import glyph_service, publish_service
from tools.utils import fs_util


def main():
    fs_util.delete_dir(path_define.outputs_dir)
    fs_util.delete_dir(path_define.releases_dir)

    for font_size in configs.font_sizes:
        fragments = glyph_service.load_fragments(font_size)
        glyph_service.make_patterns(font_size, fragments)
        publish_service.make_release_zip(font_size)


if __name__ == '__main__':
    main()
