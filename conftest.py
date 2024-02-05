import pytest
import zipfile
import shutil
import os


@pytest.fixture(autouse=True)
def archive():
    # создание архива
    files_zip = zipfile.ZipFile("tmp/file.zip", 'w')
    files_zip.write("tmp/Sample.csv", arcname='Sample.csv', compress_type=zipfile.ZIP_DEFLATED)
    files_zip.write("tmp/sample3.xlsx", arcname='sample3.xlsx', compress_type=zipfile.ZIP_DEFLATED)
    files_zip.write("tmp/Браузерные_расширения.pdf", arcname='PDF.pdf', compress_type=zipfile.ZIP_DEFLATED)
    files_zip.close()

    # Создание папки и перемещение в resources
    new_folder_path = "resources"
    os.makedirs(new_folder_path, exist_ok=True)
    shutil.move("tmp/file.zip", "resources/file.zip")
    yield
    shutil.rmtree("resources")