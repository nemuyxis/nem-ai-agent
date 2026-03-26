import os
import subprocess
from google.genai import types

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Executes a specified Python file within the working directory and returns its output",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the Python file to run, relative to the working directory",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                items=types.Schema(
                    type=types.Type.STRING,
                ),
                description="Optional list of arguments to pass to the Python script",
            ),
        },
        required=["file_path"],
    ),
)

def run_python_file(working_directory, file_path, args=None):
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(working_dir_abs, file_path))
        if os.path.isfile(target_dir):
            valid_target_dir = os.path.commonpath([working_dir_abs, target_dir])
            if valid_target_dir == working_dir_abs:
                if file_path.endswith(".py"):
                    command = ["python", target_dir]
                    if args is not None:
                        command.extend(args)
                    Completedrun = subprocess.run(command, capture_output=True, text=True, timeout=30)
                    run_out = ""
                    if Completedrun.returncode != 0:
                        run_out = f"Process exited with code {Completedrun.returncode}. "
                    if Completedrun.stderr == '' and Completedrun.stdout =='':
                        run_out += "No output produced. "
                    else:
                        run_out += f'STDOUT: {Completedrun.stdout} STDERR: {Completedrun.stderr}'
                    print(run_out)
                    return run_out
                else:
                    print(f'Error: "{file_path}" is not a Python file')
                    return f'Error: "{file_path}" is not a Python file'
            else:
                print(f'Cannot execute "{file_path}" as it is outside the permitted working directory')
                return f'Cannot execute "{file_path}" as it is outside the permitted working directory'
        else:
            print(f'Error: "{file_path}" does not exist or is not a regular file')
            return f'Error: "{file_path}" does not exist or is not a regular file'
    except Exception as e:
        return f"Error: executing Python file: {e}"
