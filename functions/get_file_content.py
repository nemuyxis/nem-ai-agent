import os

MAX_CHAR = 10000

def get_file_content(working_directory, file_path):
    working_dir_abs = os.path.abspath(working_directory)
    target_dir = os.path.normpath(os.path.join(working_dir_abs, file_path))
    if os.path.isfile(target_dir):
        valid_target_dir = os.path.commonpath([working_dir_abs, target_dir])
        if valid_target_dir == working_dir_abs:
            file_content_string = ""
            with open(target_dir, "r") as f:
                file_content_string = f.read(MAX_CHAR)
                f_len = len(file_content_string)
                if f.read(1):
                    content = f'[...File "{file_path}" truncated at {MAX_CHAR} characters]'
                    file_content_string += f'[...File "{file_path}" truncated at {MAX_CHAR} characters]'
            if f_len < 10000:
                print(file_content_string)
            else:
                print(f"File length: {f_len}/n{content}")
        else:
            print(f'Error: Cannot read "{file_path}" as it is outside the permitted working directory')
    else:
        print(f'Error: File not found or is not a regular file: "{file_path}"')
