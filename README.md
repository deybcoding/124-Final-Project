# SNOL Interpreter Project

This is a custom interpreter for the SNOL (Simple Number-Only Language) specification, written in Python, with user-friendly features, error handling, command history, colorized output, variable listing, and more.

---

## Project Structure

The project is organized into the following modules:

- **main.py**: The entry point of the application  
- **constants.py**: Contains color codes and configuration settings  
- **utils.py**: Utility functions for output formatting  
- **validators.py**: Input validation functions for variables and literals  
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

- `var = expr` : Assigns a value or result to a variable
- `BEG var` : Prompts for user input
- `PRINT var` : Displays value of a variable
- `expr1 + expr2` : Arithmetic expressions (also `-`, `*`, `/`, `%`)
- `EXIT!` : Terminates the interpreter

### Special Features

- `HISTORY` : Shows entered commands
- `LISTVARS` : Lists all defined variables and their types
- `HELP` : Displays supported commands and usage help

---

## Authors

- Dave Royo
- Mark Pena
- Dave Dagohoy
- Johnric Apolinario