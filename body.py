import tkinter as tk
from tkinter import ttk


class Body(ttk.Frame):
    def __init__(self, master=None, *args, **kwargs):
        super().__init__(master, *args, **kwargs)


def main():
    print("テキストエディタ本体の大部分を定義するモジュールです。")


if __name__ == "__main__":
    main()
