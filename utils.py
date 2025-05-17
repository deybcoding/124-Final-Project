from constants import RED, GREEN, YELLOW, BLUE, RESET, COLOR_OUTPUT

# Utility functions for output
def cprint(text, color=RESET):
    """
    Print text to the console with optional color formatting.
    If COLOR_OUTPUT is False, prints without color.
    """
    if COLOR_OUTPUT:
        print(f"{color}{text}{RESET}")
    else:
        print(text)