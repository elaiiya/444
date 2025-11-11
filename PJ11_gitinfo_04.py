# PJ11_gitinfo_04.py
# Студент №4 — Git Build Info Script

import subprocess
from datetime import datetime

def get_git_commit_hash():
    """Получает хэш последнего коммита."""
    try:
        commit_hash = subprocess.check_output(['git', 'rev-parse', 'HEAD']).decode('utf-8').strip()
        return commit_hash
    except subprocess.CalledProcessError:
        return "Git commit не найден"

def get_git_commit_date():
    """Получает дату последнего коммита."""
    try:
        commit_date = subprocess.check_output(['git', 'log', '-1', '--format=%cd']).decode('utf-8').strip()
        return commit_date
    except subprocess.CalledProcessError:
        return "Дата коммита не найдена"

def save_build_info():
    """Создаёт или обновляет файл build_info.txt с данными о сборке."""
    commit_hash = get_git_commit_hash()
    commit_date = get_git_commit_date()
    build_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("build_info.txt", "w", encoding="utf-8") as file:
        file.write(f"Commit hash: {commit_hash}\n")
        file.write(f"Commit date: {commit_date}\n")
        file.write(f"Build time: {build_time}\n")

    print("✅ Файл build_info.txt успешно обновлён.")

if __name__ == "__main__":
    save_build_info()
