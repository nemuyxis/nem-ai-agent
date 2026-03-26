import os
from google.genai import types

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Write into the selected file in a specified directory relative to the working directory.",
    parameters=types.Schema(
        required=["file_path", "content"],
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the file to write content to, relative to the working directory (default is the working directory itself)",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="Content to write into the selected file."
            ),
        },
    ),
)

def write_file(working_directory, file_path, content):
    working_dir_abs = os.path.abspath(working_directory)
    target_dir = os.path.normpath(os.path.join(working_dir_abs, file_path))
    valid_target_dir = os.path.commonpath([working_dir_abs, target_dir])
    if valid_target_dir == working_dir_abs:
        if os.path.isdir(target_dir):
            return f'Error: Cannot write to "{file_path}" as it is a directory'
        else:
            with open(target_dir, "w") as f:
                f.write(content)
                return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    else:
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
