import tkinter as tk
from tkinter import filedialog
import os
from menubar import Menubar
from body import TextEditor, StatusBar

class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.width = 1080
        self.height = 640
        self.geometry(f"{self.width}x{self.height}")
        self.set_filename("")
        self.menubar = Menubar(self)
        self.editor = TextEditor(self)
        self.status = StatusBar(self, "新規")
        self.set_darkmode()

    def set_filename(self, filename:str=""):
        self.filename = filename
        if(filename):
            name = os.path.basename(filename)
        else:
            name = "無題"
        self.title(name + " - エディタ")

    def on_new(self, *args):
        self.editor.delete("1.0", "end")
        self.set_filename("")
        self.status.set("新規")
        return "break"

    def on_window_new(self, *args):
        new = Application()
        return "break"

    def on_open(self, *args):
        ft = [("テキスト ファイル", "*.txt *.*"), ("すべてのファイル", "*.*")]
        filename = filedialog.askopenfilename(filetypes=ft)
        if(filename):
            with open(filename, "r", encoding="utf-8") as f:
                self.editor.set(f.read())
            self.set_filename(filename)
            self.status.set(f"開きました: {filename}")
        return "break"

    def save(self, filename, *args):
        with open(filename, "w", encoding="utf-8") as f:
            f.write(self.editor.get())
        self.status.set(f"保存しました: {filename}")

    def on_save(self, *args):
        if(self.filename):
            self.save(self.filename)
        else:
            self.on_save_as()
        return "break"

    def on_save_as(self, *args):
        ft = [("テキスト ファイル", "*.txt *.*"), ("すべてのファイル", "*.*")]
        filename = filedialog.asksaveasfilename(filetypes=ft)
        if(filename):
            self.save(filename)
            self.set_filename(filename)
        return "break"

    def set_darkmode(self):
        self.editor.set_darkmode()
        self.status.set_darkmode()


def main():
    root = Application()
    root.mainloop()


if __name__ == "__main__":
    main()
