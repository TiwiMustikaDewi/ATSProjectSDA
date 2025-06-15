import tkinter as tk
from PIL import Image, ImageTk
import os
from page_second import open_second_page
from page_project import open_third_page

def main():
    root = tk.Tk()
    root.title("Loading")
    screen_width = 360
    screen_height = 640
    root.geometry(f"{screen_width}x{screen_height}")
    root.resizable(False, False)

    # Tampilkan gambar loading
    current_dir = os.path.dirname(os.path.abspath(__file__))
    loading_path = os.path.join(current_dir, "assets", "LOADING.jpg")
    loading_img = Image.open(loading_path).resize((screen_width, screen_height), Image.Resampling.LANCZOS)
    loading_photo = ImageTk.PhotoImage(loading_img)

    canvas_loading = tk.Canvas(root, width=screen_width, height=screen_height)
    canvas_loading.pack(fill="both", expand=True)
    canvas_loading.create_image(0, 0, anchor="nw", image=loading_photo)
    canvas_loading.image = loading_photo  # Simpan referensi

    def show_welcome():
        root.destroy()
        show_welcome_window()

    root.after(2000, show_welcome)  # 2 detik loading
    root.mainloop()

def show_welcome_window():
    welcome_window = tk.Tk()
    welcome_window.title("DojoDash App")
    screen_width = 360
    screen_height = 640
    welcome_window.geometry(f"{screen_width}x{screen_height}")
    welcome_window.resizable(False, False)

    current_dir = os.path.dirname(os.path.abspath(__file__))
    image_path_1 = os.path.join(current_dir, "assets", "BERANDA.jpg")
    bg_image_1 = Image.open(image_path_1).resize((screen_width, screen_height), Image.Resampling.LANCZOS)
    bg_photo_1 = ImageTk.PhotoImage(bg_image_1)

    canvas1 = tk.Canvas(welcome_window, width=screen_width, height=screen_height)
    canvas1.pack(fill="both", expand=True)
    canvas1.create_image(0, 0, anchor="nw", image=bg_photo_1)
    canvas1.image = bg_photo_1

    start_button = tk.Button(
        welcome_window, text="START", font=("Inter", 18, "bold"),
        bg="#001366", fg="white", activebackground="#00C1F1",
        command=lambda: [welcome_window.withdraw(), open_second_page(parent=welcome_window)],
        cursor="hand2", borderwidth=0
    )
    canvas1.create_window(screen_width // 2, 540, window=start_button)

    welcome_window.mainloop()

if __name__ == "__main__":
    main()
