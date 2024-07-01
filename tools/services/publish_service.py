import zipfile

from tools import configs
from tools.configs import path_define


def make_release_zip(font_size: int):
    path_define.releases_dir.mkdir(parents=True, exist_ok=True)
    zip_file_path = path_define.releases_dir.joinpath(f'pixel-glyphs-braille-patterns-{font_size}px-v{configs.version}.zip')
    with zipfile.ZipFile(zip_file_path, 'w') as file:
        file.write(path_define.project_root_dir.joinpath('LICENSE-OFL'), 'OFL.txt')
        outputs_dir = path_define.outputs_dir.joinpath(str(font_size))
        for file_dir, _, file_names in outputs_dir.walk():
            for file_name in file_names:
                if not file_name.endswith('.png'):
                    continue
                file_path = file_dir.joinpath(file_name)
                file.write(file_path, file_path.relative_to(outputs_dir))
    print(f"Make release zip: '{zip_file_path}'")
