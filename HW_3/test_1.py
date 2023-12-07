import os
from datetime import datetime

import pytest
from HW_2.task_1 import find_text
import yaml

with open('config.yaml', encoding='utf-8') as f:
    data = yaml.safe_load(f)


@pytest.mark.usefixtures('make_folders', 'make_files', 'delete_folders')
class TestSeminar:

    def test_step_2(self):
        assert find_text(f'cd {data.get("folder_in")}; 7z a {data.get("folder_out")}/archive_1', "Everything is Ok")

    def test_step_3(self):
        assert find_text(f'cd {data.get("folder_out")}; 7z d archive_1', "Everything is Ok")


@pytest.fixture(autouse=True)
def add_stat():
    with open('stat.txt', 'a') as file:
        time = datetime.now().strftime('%Y.%m.%d %H:%M:%S')
        file_size = os.path.getsize('config.yaml')
        with open('/proc/loadavg', 'r') as f:
            cpu_stat = f.read()
        stat = f'{time}, {file_size}, {cpu_stat}\n'
        file.write(stat)


if __name__ == '__main__':
    pytest.main(["-vv"])