import os

def check_utf8_encoding(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            file.read()
        return True
    except UnicodeDecodeError:
        return False

def check_directory_for_python_files(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                is_utf8 = check_utf8_encoding(file_path)
                print(f"{file_path}: {'UTF-8 encoded' if is_utf8 else 'Not UTF-8 encoded'}")

# Replace this with the directory you want to check
directory_to_check = r"C:/Users/cetin/OneDrive/Masaüstü/ecom"
check_directory_for_python_files(directory_to_check)
