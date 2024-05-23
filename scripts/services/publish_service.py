import logging
import zipfile

from scripts import configs
from scripts.configs import path_define

logger = logging.getLogger('publish_service')


def make_release_zip(font_size: int):
    path_define.releases_dir.mkdir(parents=True, exist_ok=True)
    zip_file_path = path_define.releases_dir.joinpath(f'pixel-glyphs-braille-patterns-{font_size}px-v{configs.version}.zip')
    with zipfile.ZipFile(zip_file_path, 'w') as file:
        outputs_dir = path_define.outputs_dir.joinpath(str(font_size))
        for file_dir, _, file_names in outputs_dir.walk():
            for file_name in file_names:
                if not file_name.endswith('.png'):
                    continue
                file_path = file_dir.joinpath(file_name)
                arc_path = file_path.relative_to(outputs_dir)
                file.write(file_path, arc_path)
    logger.info("Make release zip: '%s'", zip_file_path)
