from zipfile import ZipFile

from loguru import logger

from tools.config import paths, project


def make_release_zip(glyph_width: int, glyph_height: int) -> None:
    paths.RELEASES_DIR.mkdir(parents=True, exist_ok=True)

    zip_file_path = paths.RELEASES_DIR.joinpath(f'pixel-glyphs-braille-patterns-{glyph_width}x{glyph_height}px-v{project.VERSION}.zip')
    with ZipFile(zip_file_path, 'w') as file:
        file.write(paths.PROJECT_ROOT_DIR.joinpath('LICENSE-OFL'), 'OFL.txt')

        outputs_dir = paths.OUTPUTS_DIR.joinpath(f'{glyph_width}x{glyph_height}')
        for file_path in sorted(outputs_dir.rglob('*.png')):
            if not file_path.is_file():
                continue
            file.write(file_path, file_path.relative_to(outputs_dir))
    logger.info('Make release zip: {!r}', str(zip_file_path))
