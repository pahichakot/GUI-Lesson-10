# Egg Timer
from tkinter import *

# Set up
root = Tk()
root.geometry("400x300")
root.title("Kitchen Timer")

# Variables
total_seconds = 0

# Functions
def countdown():
    global total_seconds

    if total_seconds >= 0:
        mins, secs = divmod(total_seconds, 60)
        timer_label.config(text=f"{mins:02d}:{secs:02d}")

        if total_seconds > 0:
            total_seconds -= 1
            root.after(1000, countdown)
        else:
            timer_label.config(text="00:00")
            timer_label.config(text="Time's Up!")

def start_timer(seconds):
    global total_seconds
    total_seconds = seconds
    countdown()

# Title
heading = Label(root, text="Egg Timer", font=("Arial", 24))
heading.pack(pady=10)

# Timer Display
timer_label = Label(root, text="00:00", font=("Arial", 40))
timer_label.pack(pady=20)

# Preset Buttons
soft = Button(root, text="Soft Boiled (3 mins)", command=lambda: start_timer(180))
soft.pack(pady=5)

medium = Button(root, text="Medium Boiled (5 mins)", command=lambda: start_timer(300))
medium.pack(pady=5)

hard = Button(root, text="Hard Boiled (10 mins)", command=lambda: start_timer(600))
hard.pack(pady=5)

# Main Loop
root.mainloop()