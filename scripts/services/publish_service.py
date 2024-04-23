import logging
import os
import zipfile

from scripts.configs import path_define
from scripts.utils import fs_util

logger = logging.getLogger('publish_service')


def make_release_zip(font_size: int):
    fs_util.make_dir(path_define.releases_dir)
    zip_file_path = os.path.join(path_define.releases_dir, f'pixel-glyphs-braille-patterns-{font_size}px.zip')
    with zipfile.ZipFile(zip_file_path, 'w') as file:
        outputs_dir = os.path.join(path_define.outputs_dir, str(font_size))
        for file_dir, _, file_names in os.walk(outputs_dir):
            for file_name in file_names:
                if not file_name.endswith('.png'):
                    continue
                file_path = os.path.join(file_dir, file_name)
                arc_path = file_path.removeprefix(f'{outputs_dir}/')
                file.write(file_path, arc_path)
    logger.info("Make release zip: '%s'", zip_file_path)
