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
