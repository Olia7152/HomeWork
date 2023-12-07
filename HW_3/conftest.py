import datetime
import os.path

import pytest
import yaml
from HW_2.task_1 import find_text

with open('config.yaml', encoding='utf-8') as f:
    data = yaml.safe_load(f)


@pytest.fixture(scope='class')
def make_folders():
    return find_text(f'mkdir -p {data.get("folder_in")} {data.get("folder_out")} {data.get("folder_ex")}', '')


@pytest.fixture(scope='class')
def delete_folders():
    yield
    return find_text(f'rm -rf {data.get("folder_in")} {data.get("folder_out")} {data.get("folder_ex")}', '')


@pytest.fixture(scope='class')
def make_files():
    return find_text(f'cd {data.get("folder_in")}; touch file_1.txt file_2.txt file_3.txt', '')


