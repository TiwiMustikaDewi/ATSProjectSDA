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

        self.canvas.create_text(20, 120, text="Division:", fill="white", font=("Inter", 10, "bold"), anchor="w")
        self.division_entry = tk.Entry(self.master, width=15, font=("Inter", 8))
        self.canvas.create_window(125, 120, window=self.division_entry)
       
        self.canvas.create_text(210, 120, text="Judges:", fill="white", font=("Inter", 10, "bold"), anchor="w")
        self.judges_entry = tk.Entry(self.master, width=10, font=("Inter", 8))
        self.canvas.create_window(300, 120, window=self.judges_entry)

        self.canvas.create_text(35, 170, text="Ao:", fill="white", font=("Inter", 10, "bold"), anchor="w")
       
        self.ao_name = tk.Entry(self.master, width=12, font=("Inter", 8))
        self.canvas.create_window(100, 170, window=self.ao_name)

        self.canvas.create_text(20, 200, text="Jurus:", fill="white", font=("Inter", 10, "bold"), anchor="w")
        self.ao_Jurus = ttk.Combobox(self.master, values=[
            "Kanku Dai", "Kanku Sho", "Bassai Dai", "Jion",
            "Empi", "Unsu", "Gojushiho Sho", "Gojushiho Dai",
            "Chinte", "Meikyo"
        ], width=9, state="readonly", font=("Inter", 8))
        self.ao_Jurus.set("Pilih Jurus")
        self.canvas.create_window(100, 200, window=self.ao_Jurus)

        self.canvas.create_text(210, 170, text="Aka:", fill="white", font=("Inter", 10, "bold"), anchor="w")
       
        self.aka_name = tk.Entry(self.master, width=12, font=("Inter", 8))
        self.canvas.create_window(287, 170, window=self.aka_name)
       
        self.canvas.create_text(200, 200, text="Jurus:", fill="white", font=("Inter", 10, "bold"), anchor="w")
        self.aka_Jurus = ttk.Combobox(self.master, values=[
            "Kanku Dai", "Kanku Sho", "Bassai Dai", "Jion",
            "Empi", "Unsu", "Gojushiho Sho", "Gojushiho Dai",
            "Chinte", "Meikyo"
        ], width=9, state="readonly", font=("Inter", 8))
        self.aka_Jurus.set("Pilih Jurus")
        self.canvas.create_window(287, 200, window=self.aka_Jurus)
        
        self.ao_score_label = tk.Label(self.master, text="0", font=("Inter", 36, "bold"), fg="white", bg="blue")
        self.canvas.create_window(125, 250, window=self.ao_score_label)
       
        self.aka_score_label = tk.Label(self.master, text="0", font=("Inter", 36, "bold"), fg="white", bg="red")
        self.canvas.create_window(300, 250, window=self.aka_score_label)

        self.ao_timer_label = tk.Label(self.master, text="0:00", font=("Inter", 12, "bold"), fg="white", bg="navy")
        self.canvas.create_window(90, 310, window=self.ao_timer_label)
       
        self.aka_timer_label = tk.Label(self.master, text="0:00", font=("Inter", 12, "bold"), fg="white", bg="darkred")
        self.canvas.create_window(265, 310, window=self.aka_timer_label)

        self._create_button("-1", lambda: self.change_score("ao", -1), 60, 350, width=3)
        self._create_button("+1", lambda: self.change_score("ao", 1), 120, 350, width=3)
        self._create_button("-1", lambda: self.change_score("aka", -1), 232, 350, width=3)
        self._create_button("+1", lambda: self.change_score("aka", 1), 300, 350, width=3)

        self._create_button("Shikkaku", lambda: self.disqualify("ao"), 55, 390, width=7, bg="midnightblue", fg="white")
        self._create_button("Kiken", lambda: self.retire("ao"), 130, 390, width=7, bg="midnightblue", fg="white")
        self._create_button("Shikkaku", lambda: self.disqualify("aka"), 228, 390, width=7, bg="darkred", fg="white")
        self._create_button("Kiken", lambda: self.retire("aka"), 300, 390, width=7, bg="darkred", fg="white")

        self.ao_start_btn = self._create_button("START", self.start_ao_timer, 90, 430, width=7, bg="limegreen")
        self.aka_start_btn = self._create_button("START", self.start_aka_timer, 270, 430, width=7, bg="limegreen")
        
        self.toggle_btn = self._create_button("SHOW/HIDE\nSTOPWATCH", self.toggle_stopwatch, 180, 490, width=15, bg="limegreen")
        self.done_btn = self._create_button("DONE", self.save_scores, 100, 530, width=7, bg="limegreen")
        self.reset_btn = self._create_button("RESET", self.reset_all, 255, 530, width=7, bg="limegreen")
        self.back_btn = self._create_button("CLOSE", self.go_back, 180, 550, width=10, bg="red", fg="white")

