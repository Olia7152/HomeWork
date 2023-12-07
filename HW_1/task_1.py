import subprocess


def find_text(command: str, text: str):
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, encoding='UTF-8')
    out = result.stdout
    if result.returncode == 0:
        if text in out:
            return True
        else:
            return False


print(find_text('cat /etc/os-release', 'jammy'))

if __name__ == "__main__":
    find_text("cd /home/user/folder_ex; touch file_1", "")