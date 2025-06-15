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

