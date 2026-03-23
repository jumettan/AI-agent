import os
import subprocess
from google.genai import types

def run_python_file(working_directory, file_path, args=None):
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.normpath(os.path.join(abs_working_dir, file_path))
    
    try:
        if os.path.commonpath([abs_working_dir,abs_file_path]) != abs_working_dir:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
           
        if not os.path.isfile(abs_file_path):
            return f'Error: "{file_path}" does not exist or is not a regular file'
        if not abs_file_path.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file'
        
        command = ["python", abs_file_path]
        
        if args:
            command.extend(args)
        
        completedProcess = subprocess.run(
            command,
            cwd=abs_working_dir,
            capture_output=True,
            text = True,
            timeout = 30
            )
        output = []
        if completedProcess.returncode != 0:
            output.append(f"Process exited with code {completedProcess.returncode}")
        if completedProcess.stdout == "" and completedProcess.stderr == "":
            output.append(f"No output produced")
        if completedProcess.stdout:
            output.append(f"STDOUT:\n{completedProcess.stdout}")
        if completedProcess.stderr:
            output.append(f"STDERR:\n{completedProcess.stderr}")
        return "\n".join(output)
    except Exception as e:
        return f"Error: executing Python file: {e}"
    
schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description = "Run current python file in the current working directory",
    parameters = types.Schema(
        type=types.Type.OBJECT,
        properties ={
            "file_path" : types.Schema(
                type=types.Type.STRING,
                description="Python file path to list files from, relative to the working directory (default is the working directory itself)",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                items=types.Schema(
                    type=types.Type.STRING,
                )
            )
        },
        required = ["file_path"]
    )
)