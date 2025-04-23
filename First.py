import random
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def get_computer_choice():
    return random.choice(["Rock", "Paper", "Scissors"])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        return "You win!"
    else:
        return "You lose!"

def play(user_choice):
    computer_choice = get_computer_choice()
    result = determine_winner(user_choice, computer_choice)
    result_text.set(f"You: {user_choice} | Computer: {computer_choice}\n{result}")

# Set up the main window
window = tk.Tk()
window.title("Rock, Paper, Scissors")
window.geometry("400x300")
window.configure(bg="#2E3440")  # Dark background

style = ttk.Style(window)
window.tk.call("source", "azure.tcl")  # Optional: Use a ttk theme file if available
style.theme_use("default")

style.configure("TButton",
                font=("Segoe UI", 12),
                padding=10,
                relief="flat",
                background="#88C0D0",
                foreground="#2E3440")
style.map("TButton",
          background=[("active", "#81A1C1")])

# Title
title = tk.Label(window, text="Rock, Paper, Scissors", font=("Segoe UI", 18, "bold"), bg="#2E3440", fg="#ECEFF4")
title.pack(pady=20)

# Buttons
button_frame = ttk.Frame(window)
button_frame.pack(pady=10)

ttk.Button(button_frame, text="Rock", command=lambda: play("Rock")).grid(row=0, column=0, padx=10)
ttk.Button(button_frame, text="Paper", command=lambda: play("Paper")).grid(row=0, column=1, padx=10)
ttk.Button(button_frame, text="Scissors", command=lambda: play("Scissors")).grid(row=0, column=2, padx=10)

# Result Display
result_text = tk.StringVar()
result_label = tk.Label(window, textvariable=result_text, font=("Segoe UI", 12), bg="#2E3440", fg="#D8DEE9", wraplength=350, justify="center")
result_label.pack(pady=30)

window.mainloop()
