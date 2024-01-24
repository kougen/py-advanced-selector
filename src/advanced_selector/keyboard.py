import os
if os.name == 'nt':
    import msvcrt as gch
elif os.name == 'posix':
    import getch as gch
else:
    raise Exception('Unsupported OS')

OS_ESCAPE = b'\x1b' if os.name == 'nt' else '\x1b'       
KEYS_ENTER = ('enter', b'\r', b'\n')
KEYS_UP = ('up',b'k', 'k')
KEYS_DOWN = ('down', 'j', b'j')
KEYS_SELECT = (' ', b' ', b'x', 'x')
KEYS_ESC = ('esc', f'{OS_ESCAPE}{OS_ESCAPE}')
KEYS_SEARCH = (b's', b'f', 's', 'f')
KEYS_ALL = (b'a', 'a')


class KeyboardHandler:
    selected_key = None  # type: None | str
    
    def __init__(self):
        pass

    def get_key(self):
        first_char = gch.getch()

        if first_char == b'\xe0':
            second_char = gch.getch()
            self.selected_key = {b'H': 'up', b'P': 'down', b'M': 'right', b'K': 'left'}[second_char]
            return self.selected_key
        
        if first_char == OS_ESCAPE:
            second_char = gch.getch()
            if second_char == OS_ESCAPE:
                self.selected_key = KEYS_ESC[0]  # Single Escape key press
            else:
                self.selected_key = {'[A': 'up', '[B': 'down', '[C': 'right', '[D': 'left'}[second_char + gch.getch()]
            return self.selected_key
        elif first_char == '\r' or first_char == '\n':
            self.selected_key = 'enter'
        else:
            self.selected_key = first_char

        return self.selected_key
