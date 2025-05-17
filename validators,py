import re
from constants import RED
from utils import cprint

# Check if a variable name is valid
def is_valid_var_name(token):
    return re.fullmatch(r'[a-zA-Z][a-zA-Z0-9]*', token) and token not in {"PRINT", "BEG", "EXIT", "HISTORY", "LISTVARS", "HELP"}

# Literal matchers
def is_integer(token):
    return re.fullmatch(r'-?\d+', token)

def is_float(token):
    return re.fullmatch(r'-?\d+\.\d+', token)

# Type recognition
def parse_value(token, variables):
    if is_integer(token):
        return int(token), 'int'
    elif is_float(token):
        return float(token), 'float'
    elif token in variables:
        return variables[token]
    elif is_valid_var_name(token):
        cprint(f"SNOL> Error! Variable [{token}] is not defined. Make sure it's assigned before use.", RED)
        return None, None
    else:
        cprint(f"SNOL> Unknown word [{token}]", RED)
        return None, None