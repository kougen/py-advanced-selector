from .keyboard import KEYS_ENTER, KEYS_ESC
from .menu import Menu, FunctionItem
from .xlib import clear
from .colors import colorize

class MenuWrapper(Menu):
    def __init__(self, title: str, options: list, indicator='->', selected=0, shown_content=15):
        super().__init__(title, options, None, None, indicator, selected, shown_content)

    def show(self, parent=''):
        if parent != '':
            title = f'{parent} -> {self.title}'
        else:
            title = self.title
        move = KEYS_ENTER[0]
        while move not in KEYS_ESC:
            clear()
            print(f'{title}')
            for index in range(self.page * self.shown_content, self.shown_content + self.page * self.shown_content):
                if index < len(self.options):
                    option = self.options[index]
                    if index == self.selected:
                        print(colorize(f'{self.indicator} {option}'))
                    else:
                        print(f'{self.indicator_space} {option}')
            move = self.action_check()
            if move in KEYS_ENTER:
                if type(self.options[self.selected]) == FunctionItem:
                    func = self.options[self.selected]  # type: FunctionItem
                    func.callable()

                if isinstance(self.options[self.selected], Menu):
                    menu = self.options[self.selected]  # type: Menu
                    menu.show(self.title)
