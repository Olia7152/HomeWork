import pytest
from HW_1.task_1 import find_text

folder_in = '/home/user/folder_in'
folder_out = '/home/user/folder_out'


def test_step_1():
    assert find_text(f'cd {folder_in}; 7z a {folder_out}/archive_2', "Everything is Ok")


def test_step_2():
    assert find_text(f'cd {folder_out}; 7z l archive_2.7z', "3 files")


def test_step_4():
    assert find_text(f'cd {folder_out}; 7z x archive_2.7z', "Everything is Ok")


if __name__ == '__main__':
    pytest.main(["-vv"])
