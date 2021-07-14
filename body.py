import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText


class TextEditor(ScrolledText):
    def __init__(self, master=None, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
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


class StatusBar(ttk.Label):
    def __init__(self, master=None, *args, **kwargs):
        self.status = tk.StringVar()
        super().__init__(master, textvariable=self.status, relief=tk.SOLID, *args, **kwargs)
        self.pack(side=tk.BOTTOM, fill=tk.X)

    def set(self, text:str="", clear:bool=True, cleartime:int=3000):
        self.status.set(text)
        if(clear == True):
            self.after(cleartime, lambda:self.status.set(""))


def main():
    print("テキストエディタ本体のメイン部分を定義するモジュールです。")


if __name__ == "__main__":
    main()
