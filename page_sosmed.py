import tkinter as tk
from PIL import Image, ImageTk
import tkinter.messagebox as messagebox
import os

def open_sosmed_page(parent=None):
    from page_second import open_second_page

    if parent is None:
        parent = tk.Tk()
