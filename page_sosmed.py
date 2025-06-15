import tkinter as tk
from PIL import Image, ImageTk
import tkinter.messagebox as messagebox
import os

def open_sosmed_page(parent=None):
    from page_second import open_second_page

    if parent is None:
        parent = tk.Tk()
    sosmed_window = tk.Toplevel(parent)
    sosmed_window.title("Sosial Media")
    screen_width = 360
    screen_height = 640
    sosmed_window.geometry(f"{screen_width}x{screen_height}")
    sosmed_window.resizable(False, False)

    current_dir = os.path.dirname(os.path.abspath(__file__))
    image_path = os.path.join(current_dir, "assets", "SOSMED.jpg")

    bg_image = Image.open(image_path)
    bg_image = bg_image.resize((screen_width, screen_height), Image.Resampling.LANCZOS)
    bg_photo = ImageTk.PhotoImage(bg_image)

    canvas = tk.Canvas(sosmed_window, width=screen_width, height=screen_height)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, anchor="nw", image=bg_photo)
    sosmed_window.bg_photo = bg_photo
