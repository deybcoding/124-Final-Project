from constants import RED, GREEN, BLUE
from utils import cprint
from validators import is_valid_var_name
from evaluator import evaluate_expression
from commands import (
    handle_input, handle_print, handle_assignment, 
    handle_expression, show_history, list_variables, show_help
)
import sys
import os

class SNOLInterpreter:
    """
    Core SNOL interpreter class.
    Handles command processing, variable storage, and command history.
    """
    def __init__(self):
        """
        Initialize interpreter state: variables and command history.
        """
        self.variables = {}
        self.command_history = []
    
    # Interpret and dispatch a command
    def process_command(self, command):
        """
        Interpret and dispatch a single SNOL command.
        Handles built-in commands, variable assignment, expressions, and error reporting.
        """
        command = command.strip()
        if not command:
            return
        
        self.command_history.append(command)
        
        if command == "EXIT!":
            cprint("Interpreter is now terminated…", BLUE)
            sys.exit()
        elif command == "HISTORY":
            show_history(self.command_history)
        elif command == "LISTVARS":
            list_variables(self.variables)
        elif command == "HELP":
            show_help()
        elif command == "CLEAR":
            os.system("cls" if os.name == "nt" else "clear")
            from main import print_welcome_message
            print_welcome_message()
        elif command.startswith("BEG "):
            handle_input(command, self.variables)
        elif command.startswith("PRINT "):
            handle_print(command, self.variables)
        elif '=' in command:
            handle_assignment(command, self.variables)
        elif any(op in command for op in ['+', '-', '*', '/', '%']):
            handle_expression(command, self.variables)
        elif is_valid_var_name(command):
            if command in self.variables:
                value, _type = self.variables[command]
                cprint(f"SNOL> [{command}] = {value}", GREEN)
            else:
                cprint(f"SNOL> Error! [{command}] is not defined!", RED)
        else:
            cprint("SNOL> Unknown command! Does not match any valid command of the language.", RED)
    
    def run(self):
        """
        Start the SNOL interpreter REPL loop.
        Accepts user input and processes commands until termination.
        """
        cprint("The SNOL environment is now active, you may proceed with giving your commands.", BLUE)
        while True:
            try:
                command = input("Command: ")
                self.process_command(command)
            except KeyboardInterrupt:
                cprint("\nInterpreter terminated by user.", BLUE)
                break
