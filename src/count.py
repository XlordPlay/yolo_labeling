import os

def remove_empty_files_and_count_non_empty(directory):
    non_empty_count = 0

    # Проход по всем файлам в указанной директории
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        # Проверка, является ли файл текстовым и существует ли он
        if os.path.isfile(file_path) and filename.endswith('.txt'):
            # Проверка размера файла
            if os.path.getsize(file_path) == 0:
                print(f"Removing empty file: {file_path}")
                os.remove(file_path)  # Удаление пустого файла
            else:
                non_empty_count += 1  # Увеличение счетчика непустых файлов

    print(f"Total non-empty text files: {non_empty_count}")

# Пример использования
directory_path = 'labels/'  # Замените на путь к вашей директории
remove_empty_files_and_count_non_empty(directory_path)
