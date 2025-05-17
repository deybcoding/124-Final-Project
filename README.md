# SNOL Interpreter Project

A custom interpreter for the SNOL (Simple Number-Only Language) specification, written in Python. Features include user-friendly interface, error handling, command history, colorized output, variable listing, and more.

---

## Project Structure

The project is organized into the following modules:

- **main.py**: Entry point of the application
- **constants.py**: Color codes and configuration settings
- **utils.py**: Utility functions for output formatting
- **validators.py**: Input validation for variables and literals
- **evaluator.py**: Expression evaluation logic for arithmetic operations
- **commands.py**: Command processing functions (BEG, PRINT, etc.)
- **interpreter.py**: Core interpreter class and main processing logic

---

## Features

- Input/output operations with colorized terminal output
- Arithmetic operations (`+`, `-`, `*`, `/`, `%`)
- Variable assignment and type checking
- Command history tracking
- Variable listing
- Help command for user assistance
- Error handling for various edge cases

---

## Requirements

- Python 3.6 or higher
- No external dependencies required

---

## How to Run

```bash
python main.py
```

---

## SNOL Commands

- `var = expr` &mdash; Assigns a value or result to a variable
- `BEG var` &mdash; Prompts for user input
- `PRINT var` &mdash; Displays value of a variable
- `expr1 + expr2` &mdash; Arithmetic expressions (also `-`, `*`, `/`, `%`)
- `EXIT!` &mdash; Terminates the interpreter

---

## Special Features

- `HISTORY` &mdash; Shows entered commands
- `LISTVARS` &mdash; Lists all defined variables and their types
- `HELP` &mdash; Displays supported commands and usage help

---

## Authors

- Dave Royo
- Mark Pena
- Dave Dagohoy
- Johnric Apolinario

