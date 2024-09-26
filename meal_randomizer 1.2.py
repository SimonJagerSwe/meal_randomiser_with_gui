# Imports
import random
import tkinter as tk
# from InquirerPy import inquirer   # probably not necessary with GUI

class MyGUI:

    def __init__(self):
        
        self.window = tk.Tk()

        self.window.mainloop()


# Setup primary window
window = tk.Tk()
window.geometry('900x600')
window.title('The Magic Meal Randomizer 1.2')
welcome = tk.Label(window, text = 'Welcome to the world famous Magic Meal Randomizer!\nBrought to you by Puzzles United Inc.', font = ('Ariel', 18))
welcome.pack(padx = 20, pady = 20)


# Main menu choice buttons
operation_prompt = tk.Label(window, text = 'Which of the following will you be doing today?', font = ('Ariel', 14))
operation_prompt.pack(padx = 20, pady = 20)

button_frame = tk.Frame(window)
button_frame.columnconfigure(0, weight = 1)
button_frame.columnconfigure(1, weight = 1)
button_frame.columnconfigure(2, weight = 0)

btn_1 = tk.Button(button_frame, text = 'Find a meal', font = ('Ariel', 16))
btn_1.grid(row = 0, column = 0, sticky = tk.W + tk.E)

btn_2 = tk.Button(button_frame, text = 'See list of meals', font = ('Ariel', 16))
btn_2.grid(row = 0, column = 1, sticky = tk.W + tk.E)

btn_3 = tk.Button(button_frame, text = 'Add a new meal', font = ('Ariel', 16))
btn_3.grid(row = 0, column = 2, sticky = tk.W + tk.E)

btn_4 = tk.Button(button_frame, text = 'Exit', font = ('Ariel', 16))
btn_4.grid(row = 1, column = 1, sticky = tk.W + tk.E)

button_frame.pack(padx = 10, pady = 30)


# Run this bad boy
window.mainloop()