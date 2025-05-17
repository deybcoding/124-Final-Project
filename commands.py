from constants import RED, GREEN, BLUE, YELLOW, VERBOSE_OUTPUT
from utils import cprint
from validators import is_valid_var_name, is_integer, is_float
from evaluator import evaluate_expression

# Command: BEG var
def handle_input(command, variables):
    parts = command.split()
    if len(parts) != 2 or not is_valid_var_name(parts[1]):
        cprint("SNOL> Unknown command! Does not match any valid command of the language.", RED)
        return
    var = parts[1]
    cprint(f"SNOL> Please enter value for [{var}]:", BLUE)
    user_input = input("Input: ").strip()
    if is_integer(user_input):
        variables[var] = (int(user_input), 'int')
    elif is_float(user_input):
        variables[var] = (float(user_input), 'float')
    else:
        cprint("SNOL> Error! Invalid number format.", RED)

# Command: PRINT var
def handle_print(command, variables):
    parts = command.split()
    if len(parts) != 2:
        cprint("SNOL> Unknown command! Does not match any valid command of the language.", RED)
        return
    var = parts[1]
    if var in variables:
        value, vtype = variables[var]
        if VERBOSE_OUTPUT:
            cprint(f"SNOL> [{var}] = {value} ({vtype})", GREEN)
        else:
            cprint(f"SNOL> [{var}] = {value}", GREEN)
    elif is_integer(var) or is_float(var):
        cprint(f"SNOL> [{var}] = {var}", GREEN)
    elif is_valid_var_name(var):
        cprint(f"SNOL> Error! [{var}] is not defined!", RED)
    else:
        cprint(f"SNOL> Unknown word [{var}]", RED)

# Command: var = expr
def handle_assignment(command, variables):
    if '=' not in command:
        cprint("SNOL> Unknown command! Does not match any valid command of the language.", RED)
        return
    left, right = command.split('=', 1)
    var = left.strip()
    expr = right.strip()
    if not is_valid_var_name(var):
        cprint(f"SNOL> Unknown word [{var}]", RED)
        return
    result, result_type = evaluate_expression(expr, variables)
    if result is not None:
        variables[var] = (result, result_type)

# Simple expression handling
def handle_expression(command, variables):
    result, _ = evaluate_expression(command, variables)
    # No output required for successful expression

# Built-in extras
def show_history(command_history):
    cprint("SNOL> You've entered the following commands:", YELLOW)
    for i, cmd in enumerate(command_history, 1):
        print(f"{i}. {cmd}")

def list_variables(variables):
    cprint("SNOL> Currently defined variables:", YELLOW)
    for k, (v, t) in variables.items():
        print(f"[{k}] = {v} ({t})")

def show_help():
    cprint("SNOL> Supported SNOL commands:", YELLOW)
    print("  - var = expr        : Assigns a value or result to a variable")
    print("  - BEG var           : Prompts for user input")
    print("  - PRINT var         : Displays value of a variable")
    print("  - expr1 + expr2     : Arithmetic expressions (also -, *, /, %)")
    print("  - EXIT!             : Terminates the interpreter")
    print("  - HISTORY           : Shows entered commands")
    print("  - LISTVARS          : Lists all defined variables")
    print("  - HELP              : Displays this help message")