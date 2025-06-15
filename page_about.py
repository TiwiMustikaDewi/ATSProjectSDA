import tkinter as tk
from PIL import Image, ImageTk
import tkinter.messagebox as messagebox
import os

def open_about_page(parent=None):
    from page_second import open_second_page

    if parent is None:
        parent = tk.Tk()

    about_window = tk.Toplevel(parent)
    about_window.title("About")
    screen_width = 360
    screen_height = 640
    about_window.geometry(f"{screen_width}x{screen_height}")
    about_window.resizable(False, False)

    current_dir = os.path.dirname(os.path.abspath(__file__))
    image_path = os.path.join(current_dir, "assets", "ABOUT.jpg")

    bg_image = Image.open(image_path)
    bg_image = bg_image.resize((screen_width, screen_height), Image.Resampling.LANCZOS)
    bg_photo = ImageTk.PhotoImage(bg_image)

    canvas = tk.Canvas(about_window, width=screen_width, height=screen_height)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, anchor="nw", image=bg_photo)
    about_window.bg_photo = bg_photo 


    def go_back():
        about_window.destroy()
        open_second_page(parent=parent)

    back_button = tk.Button(about_window, text="> back", font=("Inter", 10, "bold"),
                            bg="#35216B", fg="white", activebackground="#8176E0",
                            command=go_back, cursor="hand2", borderwidth=0)
    canvas.create_window(35, 25, window=back_button)
