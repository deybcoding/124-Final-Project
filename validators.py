import re
from constants import RED
from utils import cprint

def is_valid_var_name(token):
    """
    Check if a token is a valid SNOL variable name.
    Variable names must start with a letter and contain only alphanumeric characters.
    Reserved words are not allowed as variable names.
    """
    return re.fullmatch(r'[a-zA-Z][a-zA-Z0-9]*', token) and token not in {"PRINT", "BEG", "EXIT", "HISTORY", "LISTVARS", "HELP"}

def is_integer(token):
    """
    Check if a token represents a valid integer literal.
    """
    return re.fullmatch(r'-?\d+', token)

def is_float(token):
    """
    Check if a token represents a valid floating-point literal.
    """
    return re.fullmatch(r'-?\d+\.\d+', token)

# Type recognition
def parse_value(token, variables):
    """
    Parse a token and determine its value and type.
    Handles integer, float, and variable lookups.
    Prints error messages for undefined variables or unknown tokens.
    Returns (value, type) or (None, None) on error.
    """
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