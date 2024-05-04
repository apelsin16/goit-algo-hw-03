import os
import shutil
import argparse

def copy_files(source_dir, dest_dir):
    # Перевірка наявності та створення директорії призначення
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    # Читання вихідної директорії
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            source_file_path = os.path.join(root, file)
            # Отримання розширення файлу
            _, extension = os.path.splitext(file)
            # Створення піддиректорії на основі розширення
            subdir = os.path.join(dest_dir, extension[1:])
            if not os.path.exists(subdir):
                os.makedirs(subdir)
            # Копіювання файлу до піддиректорії
            dest_file_path = os.path.join(subdir, file)
            try:
                shutil.copy(source_file_path, dest_file_path)
                print(f"Copied {source_file_path} to {dest_file_path}")
            except Exception as e:
                print(f"Error copying {source_file_path} to {dest_file_path}: {e}")

def main():
    # Парсинг аргументів командного рядка
    parser = argparse.ArgumentParser(description="Copy and sort files recursively")
    parser.add_argument("source_dir", help="Source directory path")
    parser.add_argument("dest_dir", nargs="?", default="dist", help="Destination directory path")
    args = parser.parse_args()

    source_dir = args.source_dir
    dest_dir = args.dest_dir

    # Виклик функції копіювання файлів
    copy_files(source_dir, dest_dir)

if __name__ == "__main__":
    main()
