import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import csv
import os
import time


class JurusScoringApp(tk.Frame):
    def __init__(self, master, parent=None):
        super().__init__(master)
        self.master = master
        self.parent = parent


        self.ao_score = 0
        self.aka_score = 0
        self.ao_time = 0
        self.aka_time = 0
        self.ao_running = False
        self.aka_running = False
        self.ao_start_time = None
        self.aka_start_time = None
        self.stopwatch_visible = True
        self.ao_started = False
        self.aka_started = False


        self.setup_ui()
        self.update_timers()
    def setup_ui(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        bg_path = os.path.join(current_dir, "assets", "gradasi.jpg")
        bg_image = Image.open(bg_path).resize((360, 640))
        self.bg_photo = ImageTk.PhotoImage(bg_image)


        self.canvas = tk.Canvas(self, width=360, height=640)
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_image(0, 0, anchor="nw", image=self.bg_photo)


        self.canvas.create_rectangle(10, 150, 175, 450, fill="blue", outline="")
        self.canvas.create_rectangle(185, 150, 350, 450, fill="red", outline="")

