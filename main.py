# SNOL Interpreter with Enhancements
# Author: Group 4
# Description: This is a custom interpreter for the SNOL (Simple Number-Only Language)
#              specification, written in Python, with user-friendly features, error
#              handling, command history, colorized output, variable listing, and more.

from constants import YELLOW
from utils import cprint
from interpreter import SNOLInterpreter

def print_welcome_message():
    """
    Print the welcome message and list all supported SNOL commands and features.
    """
    cprint("""
Welcome to the SNOL Interpreter! Here are the supported commands:

Main SNOL Commands:
  - var = expr        : Assigns a value or result to a variable
  - BEG var           : Prompts for user input
  - PRINT var         : Displays value of a variable
  - expr1 + expr2     : Arithmetic expressions (also -, *, /, %)
  - EXIT!             : Terminates the interpreter

Special Features:
  - HISTORY           : Shows entered commands
  - LISTVARS          : Lists all defined variables and their types
  - HELP              : Displays supported commands and usage help
  - CLEAR             : Clears the console

Note: SNOL is case-sensitive. Use commands exactly as shown.
""", YELLOW)

# Main loop
def main():
    """
    Entry point for the SNOL interpreter.
    Prints the welcome message and starts the interpreter loop.
    """
    print_welcome_message()
    interpreter = SNOLInterpreter()
    interpreter.run()

if __name__ == "__main__":
    main()
