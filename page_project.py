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

        biru_img_path = os.path.join(current_dir, "assets", "BLUE.png")
        merah_img_path = os.path.join(current_dir, "assets", "RED.png")
        self.biru_photo = ImageTk.PhotoImage(Image.open(biru_img_path))
        self.merah_photo = ImageTk.PhotoImage(Image.open(merah_img_path))
        self.canvas.create_image(65, 250, image=self.biru_photo, anchor="center")
        self.canvas.create_image(240, 250, image=self.merah_photo, anchor="center")

    def _create_button(self, text, command, x, y, width=5, bg="white", fg="black"):
        button = tk.Button(self.master, text=text, command=command, width=width,
                         bg=bg, fg=fg, cursor="hand2", font=("Inter", 8))
        self.canvas.create_window(x, y, window=button)
        return button

    def change_score(self, side, amount):
        if side == "ao":
            self.ao_score += amount
            self.ao_score_label.config(text=str(self.ao_score))
        else:
            self.aka_score += amount
            self.aka_score_label.config(text=str(self.aka_score))

    def disqualify(self, side):
        messagebox.showinfo("Diskualifikasi", f"Pemain {side.upper()} terdiskualifikasi")

    def retire(self, side):
        messagebox.showinfo("Kiken", f"Pemain {side.upper()} telah mengundurkan diri")

    def start_ao_timer(self):
        if not self.ao_name.get():
            messagebox.showwarning("Peringatan", "Silakan isi nama untuk Ao terlebih dahulu")
            return
        if self.ao_Jurus.get() == "Pilih Jurus":
            messagebox.showwarning("Peringatan", "Silakan pilih Jurus untuk Ao terlebih dahulu")
            return
        self.ao_started = True
        self.aka_running = False
        self.ao_running = True
        self.ao_start_time = time.time() - self.ao_time

    def start_aka_timer(self):
        if not self.aka_name.get():
            messagebox.showwarning("Peringatan", "Silakan isi nama untuk Aka terlebih dahulu")
            return
        if self.aka_Jurus.get() == "Pilih Jurus":
            messagebox.showwarning("Peringatan", "Silakan pilih Jurus untuk Aka terlebih dahulu")
            return
        self.aka_started = True
        self.ao_running = False
        self.aka_running = True
        self.aka_start_time = time.time() - self.aka_time
        
    def update_timers(self):
        if self.ao_running:
            self.ao_time = time.time() - self.ao_start_time
            mins, secs = divmod(int(self.ao_time), 60)
            self.ao_timer_label.config(text=f"{mins}:{secs:02}")
        if self.aka_running:
            self.aka_time = time.time() - self.aka_start_time
            mins, secs = divmod(int(self.aka_time), 60)
            self.aka_timer_label.config(text=f"{mins}:{secs:02}")

        self.master.after(1000, self.update_timers)
        
    def toggle_stopwatch(self):
        self.stopwatch_visible = not self.stopwatch_visible
        state = "normal" if self.stopwatch_visible else "hidden"
        self.canvas.itemconfigure(self.ao_timer_label_id, state=state)
        self.canvas.itemconfigure(self.aka_timer_label_id, state=state)

    def save_scores(self):
        self.ao_running = False
        self.aka_running = False

        division = self.division_entry.get()
        file_path = os.path.join(os.path.dirname(__file__), "scores.csv")
        file_exists = os.path.isfile(file_path)

        rows = []
        if self.ao_started:
            rows.append([
                division,
                "AO",
                self.ao_name.get(),
                self.ao_Jurus.get(),
                self.ao_score,
                int(self.ao_time)
            ])
        if self.aka_started:
            rows.append([
                division,
                "AKA",
                self.aka_name.get(),
                self.aka_Jurus.get(),
                self.aka_score,
                int(self.aka_time)
            ])

        if not rows:
            messagebox.showwarning("Peringatan", "Belum ada pertandingan yang dimulai.")
            return

        with open(file_path, "a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            if not file_exists:
                writer.writerow(["Division", "Side", "Name", "Jurus", "Score", "Time"])
            for row in rows:
                writer.writerow(row)
        messagebox.showinfo("Simpan", "Data telah disimpan.")

    def reset_all(self):
        self.ao_score = 0
        self.aka_score = 0
        self.ao_time = 0
        self.aka_time = 0
        self.ao_running = False
        self.aka_running = False
        self.ao_started = False
        self.aka_started = False
        self.ao_score_label.config(text="0")
        self.aka_score_label.config(text="0")
        self.ao_timer_label.config(text="0:00")
        self.aka_timer_label.config(text="0:00")
        self.ao_Jurus.set("Pilih Jurus")
        self.aka_Jurus.set("Pilih Jurus")
        self.ao_name.delete(0, tk.END)
        self.aka_name.delete(0, tk.END)
        self.division_entry.delete(0, tk.END)
        self.judges_entry.delete(0, tk.END)

    def go_back(self):
        self.master.destroy()
        if self.parent:
            from page_second import open_second_page
            open_second_page(parent=self.parent)

def open_third_page(parent=None):
    window = tk.Toplevel(parent) if parent else tk.Tk()
    window.title("Project - Jurus Scoring")
    app = JurusScoringApp(window, parent=parent)
    app.pack(fill="both", expand=True)
    window.geometry("360x640")
    window.resizable(False, False)
   
    if hasattr(app, 'bg_photo'):
        app.bg_photo = app.bg_photo
    if hasattr(app, 'biru_photo'):
        app.biru_photo = app.biru_photo
    if hasattr(app, 'merah_photo'):
        app.merah_photo = app.merah_photo
   
    if not parent:
        window.mainloop()

if __name__ == "__main__":
    open_third_page()

import csv

def save_score(part, score, csv_file='scores.csv'):
    scores = {}
    try:
        with open(csv_file, 'r', newline='') as f:
            reader = csv.reader(f)
            for row in reader:
                if row:
                    scores[row[0]] = row[1]
    except FileNotFoundError:
        pass


    scores[part] = score


    with open(csv_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([part, score])

active_part = 'aka'

save_score(active_part, 90)
