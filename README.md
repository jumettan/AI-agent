<<<<<<< HEAD
This project is a self-directed AI agent that can autonomously explore, read, run, and modify code in a local directory. Think of it as a stripped-down version of something like GitHub Copilot's agent mode or Cursor's AI features.

The Core Loop (main.py)
The agent runs in a loop (up to MAX_ITERS times). Each iteration:

Sends the current message history to Gemini (Google's LLM).
Gemini either responds with text (done) or requests a function call (tool use).
If it's a function call, the agent executes it and appends the result back to the message history.
Repeat.
This is the classic ReAct pattern: the model reasons, acts, observes the result, then reasons again.

The Tools (functions/)
The agent has four tools it can call:

Tool	What it does
get_files_info	Lists files/directories
get_file_content	Reads a file
run_python_file	Executes a Python file
write_file	Writes/overwrites a file
These are registered with Gemini via call_function.py as a types.Tool, which tells the model what functions are available and what arguments they expect.

The System Prompt (prompts.py)
The system prompt is the agent's "personality and instructions." It tells Gemini to:

Start by scanning the working directory.
Make a multi-step plan before acting.
Run both tests and the app after making changes to verify correctness.
The quality of this prompt directly determines how reliably the agent solves tasks.

The Target (calculator/)
The calculator app is the sandbox the agent operates on. In this final lesson, you intentionally broke it (wrong operator precedence for +) and asked the agent to find and fix the bug on its own - no hints about which file or line.

A successful run looks like: agent lists files -> reads calculator.py -> identifies the bug -> writes the fix -> runs the app to verify -> reports success.
=======
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
>>>>>>> 81a1140 (added better description inside readme.md)
