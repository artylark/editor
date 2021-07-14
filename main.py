import tkinter as tk
from tkinter import filedialog
import os
from menubar import Menubar
from body import TextEditor, StatusBar

class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.width = 800
        self.height = 600
        self.geometry(f"{self.width}x{self.height}")
        self.filename = ""
        self.set_title()
        self.menubar = Menubar(self)
        self.editor = TextEditor(self)
        self.status = StatusBar(self)

    def set_title(self):
        if(self.filename):
            name = os.path.basename(self.filename)
        else:
            name = "無題"
        self.title(name + " - エディタ")

    def on_new(self, *args):
        self.editor.delete("1.0", "end")
        self.filename = ""
        self.set_title()
        return "break"

    def on_window_new(self, *args):
        new = Application()
        return "break"

    def on_open(self, *args):
        ft = [("テキスト ファイル", "*.txt *.py *.json"), ("すべてのファイル", "*.*")]
        filename = filedialog.askopenfilename(defaultextension="txt", filetypes=ft)
        if(filename):
            with open(filename, "r", encoding="utf-8") as f:
                self.editor.set(f.read())
            self.filename = filename
            self.set_title()
        return "break"

    def save(self, filename, *args):
        with open(filename, "w", encoding="utf-8") as f:
            f.write(self.editor.get())

    def on_save(self, *args):
        if(self.filename):
            self.save(self.filename)
        else:
            self.on_save_as()
        return "break"

    def on_save_as(self, *args):
        ft = [("テキスト ファイル", "*.txt *.py *.json"), ("すべてのファイル", "*.*")]
        filename = filedialog.asksaveasfilename(defaultextension="txt", filetypes=ft)
        if(filename):
            self.save(filename)
            self.filename = filename
            self.set_title()
        return "break"


def main():
    root = Application()
    root.mainloop()


if __name__ == "__main__":
    main()
