
import csv
import tkinter as tk
from tkinter import *
from tkinter import ttk
import ttkbootstrap as tboot
from ttkbootstrap import Style
from ttkbootstrap.constants import *
import pygame
from pygame import *
from PIL import ImageTk,Image


class MainApplication:
    def __init__(self, master):
        self.master = master
        self.master.withdraw()  # Hide the main window initially
        self.master.title("Pokemon")

        # Create a list to store the frames
        self.frames = []

        # Create a boolean flag to track if the number of frames has been set
        self.num_frames_set = False

        # Call the open_config_window method directly
        self.open_config_window()

    def open_config_window(self):
        # Create a new window for configuration
        config_window = tk.Toplevel(self.master)
        config_window.title("Configuration")

        # Create a label and entry box for the number of frames
        num_frames_label = tk.Label(config_window, text="Enter number of frames:")
        num_frames_label.pack(side=tk.LEFT, padx=(10, 0), pady=10)

        num_frames_entry = tk.Entry(config_window)
        num_frames_entry.pack(side=tk.LEFT, padx=(0, 10), pady=10)

        # Create a button to submit the number of frames and close the window
        submit_button = tk.Button(config_window, text="Submit", command=lambda: self.submit_num_frames(config_window, int(num_frames_entry.get())))
        submit_button.pack(side=tk.LEFT, padx=10, pady=10)

    def submit_num_frames(self, config_window, num_frames):
        # Destroy the configuration window
        config_window.destroy()

        # Create a self-centering frame for each frame
        for i in range(num_frames):
            poke = tk.Frame(self.master, width=280, height=941, bd=1, relief=tk.SOLID)
            poke.pack_propagate(0)
            poke.pack(side=tk.LEFT, padx=10, pady=10)
            self.frames.append(poke)

        # Calculate the total width and height required for the frames
        total_width = num_frames * (100 + 2*10)  # frame width + padx
        total_height = 100 + 2*10  # frame height + pady

        # Set the minimum size of the main application based on the total width and height required
        self.master.update()
        self.master.minsize(total_width, total_height)

        # Set the num_frames_set flag to True
        self.num_frames_set = True

        # Show the main window
        self.master.deiconify()

# Create the main tkinter window
root = tk.Tk()

# Apply the cyborg theme from ttkbootstrap
#style = Style(theme='cyborg')

# Create the main application
app = MainApplication(root)

# Start the tkinter event loop
root.mainloop()
