from blessed import Terminal

# Create the terminal instance once
term = Terminal()

def initialize():
    """Call this at the very start of main()"""
    print(term.clear + term.home)

def draw_text(x, y, text, color_func=None):
    """Prints text at a specific coordinate, optionally with color"""
    if color_func:
        text = color_func(text)
    # The '+' joins the 'move cursor' string with the 'text' string
    print(term.move_xy(x, y) + text, end='', flush=True)

def get_input(x, y, prompt):
    """Moves to a spot, asks a question, and returns the string"""
    draw_text(x, y, prompt)
    # Once the cursor is moved, we can use standard Python input()
    return input()

def clear_area(x, y):
    """Clears from the current x,y to the end of that line"""
    print(term.move_xy(x, y) + term.clear_eol, end='', flush=True)