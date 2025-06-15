import tkinter as tk
from PIL import Image, ImageTk
import os
from page_anggota import open_anggota_page
from page_project import open_third_page
from page_sosmed import open_sosmed_page 
from page_about import open_about_page  

def open_second_page(parent=None, back_callback=None):
    if parent is None:
        parent = tk.Tk()
        parent.withdraw()

    second_window = tk.Toplevel(parent)
    second_window.title("About - Weak Hero Class")
    screen_width = 360
    screen_height = 640
    second_window.geometry(f"{screen_width}x{screen_height}")
    second_window.resizable(False, False)

    current_dir = os.path.dirname(os.path.abspath(__file__))
    image_path = os.path.join(current_dir, "assets", "WELCOME.jpg")

    bg_image = Image.open(image_path)
    bg_image = bg_image.resize((screen_width, screen_height), Image.Resampling.LANCZOS)
    bg_photo = ImageTk.PhotoImage(bg_image)

    canvas = tk.Canvas(second_window, width=screen_width, height=screen_height)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, anchor="nw", image=bg_photo)
    canvas.image = bg_photo

    def open_anggota():
        second_window.destroy()
        open_anggota_page(parent=parent)

    def open_project():
        second_window.destroy()
        open_third_page(parent=parent)

    def open_social_media():
        second_window.destroy()
        open_sosmed_page(parent=parent)

    def open_about():
        second_window.destroy()
        open_about_page(parent=parent)

    def back_to_first_page():
        second_window.destroy()
        if parent is not None:
            parent.deiconify()

    back_button = tk.Button(second_window, text="> back", font=("Inter", 9, "bold"),
                            bg="#35216B", fg="white", command=back_to_first_page,
                            cursor="hand2", borderwidth=0)
    canvas.create_window(35, 25, window=back_button)

    anggota_button = tk.Button(second_window, text="> open", font=("Inter", 9, "bold"),
                               bg="#4A2C2A", fg="white",
                               command=open_anggota, cursor="hand2", borderwidth=0)
    canvas.create_window(55, 335, window=anggota_button)

    project_button = tk.Button(second_window, text="> open", font=("Inter", 9, "bold"),
                               bg="#4A2C2A", fg="white",
                               command=open_project, cursor="hand2", borderwidth=0)
    canvas.create_window(55, 247, window=project_button)

    sosmed_button = tk.Button(second_window, text="> open", font=("Inter", 9, "bold"),
                              bg="#4A2C2A", fg="white",
                              command=open_social_media, cursor="hand2", borderwidth=0)
    canvas.create_window(55, 420, window=sosmed_button)

    about_button = tk.Button(second_window, text="> open", font=("Inter", 9, "bold"),
                             bg="#4A2C2A", fg="white",
                             command=open_about, cursor="hand2", borderwidth=0)
    canvas.create_window(55, 510, window=about_button)
