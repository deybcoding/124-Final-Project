from constants import RED, GREEN, YELLOW, BLUE, RESET, COLOR_OUTPUT

# Utility functions for output
def cprint(text, color=RESET):
    if COLOR_OUTPUT:
        print(f"{color}{text}{RESET}")
    else:
        print(text)