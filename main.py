import tkinter as tk
from menubar import Menubar


class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.width = 800
        self.height = 600
        self.geometry(f"{self.width}x{self.height}")
        menubar = Menubar(self)

    def on_new(self, *args):
        return

    def on_window_new(self, *args):
        self.width = 1000
        return

    def on_open(self, *args):
        return


def main():
    root = Application()
    root.mainloop()


if __name__ == "__main__":
    main()
