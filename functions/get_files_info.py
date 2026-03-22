import os
def get_files_info(working_directory, directory="."):
    working_dir_abs = os.path.abspath(working_directory)
    target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))
    if os.path.isdir(target_dir):
        valid_target_dir = os.path.commonpath([working_dir_abs, target_dir])
        if valid_target_dir == working_dir_abs:
            str_dirs = ""
            if directory == ".":
                str_dirs = f"Result for current directory:\n"
            else:
                str_dirs = f"Result for {directory} directory:\n"
            for dir in os.listdir(target_dir):
                name = dir
                size = os.path.getsize(target_dir + "/" + dir)
                is_dir = os.path.isdir(target_dir + "/" + dir)
                str_dirs += f"  - {name}: file_size={size}, is_dir={is_dir}\n"
            print(str_dirs)
        else:
            print(f'Result for {directory} directory:\n     Error: Cannot list "{directory}" as it is outside the permitted working directory')
    else:
        print(f'Error: "{directory}" is not a directory')
    