import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText


class TextEditor(ScrolledText):
    def __init__(self, master=None, font=("MS Gothic", 12), *args, **kwargs):
        super().__init__(master, font=font, *args, **kwargs)
        self.pack(expand=True, fill=tk.BOTH)

        # Ctrl+O でファイルを開くときに意図せず改行が入力されてしまうのを防ぐため、
        # バインディングの順番を入れ替える
        bt = self.bindtags()
        self.bindtags((bt[3], *bt[:3]))

    def set(self, value:str=None):
        self.delete("1.0", "end")
        self.insert("1.0", value)

    def get(self, index1="1.0", index2="end-1c", *args, **kwargs):
        return super().get(index1=index1, index2=index2, *args, **kwargs)

    def set_darkmode(self):
        self.config(fg="#CCCCCC", bg="#1E1E1E", insertbackground="#CCCCCC", selectbackground="#264F78", bd=0,
                    padx=5, pady=5)

class StatusBar(ttk.Label):
    def __init__(self, master=None, text:str="", font=("Meiryo UI", 9), *args, **kwargs):
        self.status = tk.StringVar()
        super().__init__(master, textvariable=self.status, relief=tk.SOLID, font=font, *args, **kwargs)
        self.pack(side=tk.BOTTOM, fill=tk.X)
        self.set(text)

    def set(self, text:str="", clear:bool=True, cleartime:int=3000):
        self.status.set(text)
        if(clear == True):
            self.after(cleartime, lambda:self.status.set(""))

    def set_darkmode(self):
        self.config(foreground="#FFFFFF", background="#007ACC", relief=tk.FLAT, font=("Meiryo UI", 9, "bold"))


def main():
    print("テキストエディタ本体のメイン部分を定義するモジュールです。")


if __name__ == "__main__":
    main()
