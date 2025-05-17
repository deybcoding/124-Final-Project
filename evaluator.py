from constants import RED
from utils import cprint
from validators import parse_value

# Evaluate arithmetic expressions
def evaluate_expression(expr, variables):
    """
    Evaluate an arithmetic expression in SNOL.
    Supports single values and binary operations (+, -, *, /, %).
    Ensures operands are of the same type and handles errors.
    Returns (result, type) or (None, None) on error.
    """
    tokens = expr.split()
    if len(tokens) == 1:
        return parse_value(tokens[0], variables)
    elif len(tokens) == 3:
        left, op, right = tokens
        left_val, left_type = parse_value(left, variables)
        right_val, right_type = parse_value(right, variables)
        if left_val is None or right_val is None:
            return None, None
        if left_type != right_type:
            cprint("SNOL> Error! Operands must be of the same type in an arithmetic operation!", RED)
            return None, None
        try:
            if op == '+':
                return left_val + right_val, left_type
            elif op == '-':
                return left_val - right_val, left_type
            elif op == '*':
                return left_val * right_val, left_type
            elif op == '/':
                return left_val / right_val, left_type
            elif op == '%':
                if left_type != 'int':
                    cprint("SNOL> Error! Modulo operation only allowed for integer types!", RED)
                    return None, None
                return left_val % right_val, 'int'
            else:
                cprint("SNOL> Unknown command! Does not match any valid command of the language.", RED)
                return None, None
        except Exception as e:
            cprint(f"SNOL> Error! {str(e)}", RED)
            return None, None
    else:
        cprint("SNOL> Unknown command! Does not match any valid command of the language.", RED)
        return None, None