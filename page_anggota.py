import tkinter as tk
from PIL import Image, ImageTk
import tkinter.messagebox as messagebox
import os

def open_anggota_page(parent=None):
    from page_second import open_second_page

    if parent is None:
        parent = tk.Tk()

    anggota_window = tk.Toplevel(parent)
    anggota_window.title("Perkenalan Anggota")
    screen_width = 360
    screen_height = 640
    anggota_window.geometry(f"{screen_width}x{screen_height}")
    anggota_window.resizable(False, False)

    current_dir = os.path.dirname(os.path.abspath(__file__))
    image_path = os.path.join(current_dir, "assets", "ANGGOTA.jpg")

    bg_image = Image.open(image_path)
    bg_image = bg_image.resize((screen_width, screen_height), Image.Resampling.LANCZOS)
    bg_photo = ImageTk.PhotoImage(bg_image)

    canvas = tk.Canvas(anggota_window, width=screen_width, height=screen_height)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, anchor="nw", image=bg_photo)
    anggota_window.bg_photo = bg_photo

    def open_detail_page(name, image_filename):
        anggota_window.destroy()
        detail_window = tk.Toplevel(parent)
        detail_window.title(f"{name} - Kelompok 7")
        detail_window.geometry(f"{screen_width}x{screen_height}")
        detail_window.resizable(False, False)

        detail_image_path = os.path.join(current_dir, "assets", image_filename)
        if not os.path.exists(detail_image_path):
            print(f"⚠ Gambar tidak ditemukan: {detail_image_path}")
            return

        detail_image = Image.open(detail_image_path)
        detail_image = detail_image.resize((screen_width, screen_height), Image.Resampling.LANCZOS)
        detail_photo = ImageTk.PhotoImage(detail_image)

        canvas_detail = tk.Canvas(detail_window, width=screen_width, height=screen_height)
        canvas_detail.pack(fill="both", expand=True)
        canvas_detail.create_image(0, 0, anchor="nw", image=detail_photo)
        detail_window.detail_photo = detail_photo

        def go_back_to_anggota():
            detail_window.destroy()
            open_anggota_page(parent=parent)

        back_btn = tk.Button(detail_window, text="> back ", font=("Inter", 9, "bold"),
                             bg="#35216B", fg="white", command=go_back_to_anggota,
                             cursor="hand2", borderwidth=0)
        canvas_detail.create_window(35, 25, window=back_btn)

        name_label = tk.Label(detail_window, text=f"{name}", font=("Inter", 12, "bold"),
                              bg="#4A2C2A", fg="white", cursor="hand2")

        name_label.bind("<Button-1>", lambda e: messagebox.showinfo("What They Say?", "We have our best! Hope We get best result too!"))
        canvas_detail.create_window(screen_width // 2, 500, window=name_label)

    alyssa_button = tk.Button(anggota_window, text=">", font=("Inter", 5, "bold"),
                            bg="#598995", fg="white",
                            command=lambda: open_detail_page("What They Say?", "ALYSSA.jpg"), cursor="hand2", borderwidth=0)
    canvas.create_window(118, 316, window=alyssa_button)

    tisya_button = tk.Button(anggota_window, text=">", font=("Inter", 5, "bold"),
                          bg="#598995", fg="white",
                          command=lambda: open_detail_page("What They Say?", "TISYA.jpg"), cursor="hand2", borderwidth=0)
    canvas.create_window(287, 317, window=tisya_button)

    satriyo_button = tk.Button(anggota_window, text=">", font=("Inter", 5, "bold"),
                          bg="#598995", fg="white",
                          command=lambda: open_detail_page("What They Say?", "SATRIYO.jpg"), cursor="hand2", borderwidth=0)
    canvas.create_window(118, 510, window=satriyo_button)

    tiwi_button = tk.Button(anggota_window, text=">", font=("Inter", 5, "bold"),
                          bg="#598995", fg="white",
                          command=lambda: open_detail_page("What They Say?", "TIWI.jpg"), cursor="hand2", borderwidth=0)
    canvas.create_window(287, 510, window=tiwi_button)

    def go_back():
        anggota_window.destroy()
        open_second_page(parent=parent)

    back_button = tk.Button(anggota_window, text="> back", font=("Inter", 9, "bold"),
                            bg="#35216B", fg="white", activebackground="#8176E0",
                            command=go_back, cursor="hand2", borderwidth=0)
    canvas.create_window(35, 25, window=back_button)
