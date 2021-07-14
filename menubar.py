import tkinter as tk


class Menubar(tk.Menu):
    def __init__(self, master=None, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        master.config(menu=self)
        self.menu_file(master)

    def menu_file(self, master=None):
        file = tk.Menu(self, tearoff=0)
        self.add_cascade(menu=file, label="ファイル(F)", underline=5)
        file.add_command(command=master.on_new, label="新規(N)", underline=3, accelerator="Ctrl+N")
        master.bind_all("<Control-n>", master.on_new)
        file.add_command(command=master.on_window_new, label="新しいウィンドウ(W)", underline=9, 
                         accelerator="Ctrl+Shift+N")
        master.bind_all("<Control-N>", master.on_window_new)
        file.add_command(command=master.on_open, label="開く(O)...", underline=3, accelerator="Ctrl+O")
        master.bind_all("<Control-o>", master.on_open)

def main():
    print("メニューバーを定義するモジュールです。")


if __name__ == "__main__":
    main()
