This is an AI coding agent built with Google's Gemini 2.5 Flash model. Here's what it does:

Core concept: A CLI-based agent that takes a natural language prompt, then autonomously plans and executes actions to fulfill it — using a loop of up to 20 model calls with tool use.

How it works:

You pass a user prompt via the command line (e.g., python main.py "fix the bug in calculator.py")
The agent uses Gemini 2.5 Flash with function-calling to reason through the task
It iterates, calling tools as needed, until it produces a final text response
Available tools the agent can use:

get_files_info — list files/directories
get_file_content — read file contents
write_file — write or overwrite files
run_python_file — execute Python scripts with optional args
Sandboxing: All file/execution operations are scoped to the calculator subdirectory, which serves as the agent's working environment — a small calculator project the agent can inspect, modify, and run.

The calculator directory is essentially the agent's "workspace-under-test", containing a calculator package (pkg/calculator.py, pkg/render.py) and tests the agent can interact with.
