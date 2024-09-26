########## Imports ##########
import tkinter as tk


########## Main menu ##########
class MyGUI:
    def __init__(self):        
        self.window = tk.Tk()
        self.window.mainloop()


# Setup main menu window
def main_menu():
    window = tk.Tk()
    window.geometry('900x600')
    window.title('The Magic Meal Randomizer')
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


    # Choices
    if btn_1:
        find_meal()


########## Find meal window ##########
# Setup meal finder window
def find_meal():
    window = tk.Tk()
    window.geometry('900x600')
    window.title('Meal Randomiser')
    welcome = tk.Label(window, text = 'Meal Randomiser', font = ('Ariel', 18))
    welcome.pack(padx = 20, pady = 20)


     # Find meal choice buttons
    operation_prompt = tk.Label(window, text = 'What level of ambition do we have today?', font = ('Ariel', 14))
    operation_prompt.pack(padx = 20, pady = 20)

    button_frame = tk.Frame(window)
    button_frame.columnconfigure(0, weight = 1)
    button_frame.columnconfigure(1, weight = 1)
    button_frame.columnconfigure(2, weight = 0)

    btn_1 = tk.Button(button_frame, text = 'Easy meals', font = ('Ariel', 16))
    btn_1.grid(row = 0, column = 0, sticky = tk.W + tk.E)

    btn_2 = tk.Button(button_frame, text = 'Medium meals', font = ('Ariel', 16))
    btn_2.grid(row = 0, column = 1, sticky = tk.W + tk.E)

    btn_3 = tk.Button(button_frame, text = 'Ambitious meals', font = ('Ariel', 16))
    btn_3.grid(row = 0, column = 2, sticky = tk.W + tk.E)

    btn_4 = tk.Button(button_frame, text = 'Back to main menu', font = ('Ariel', 16))
    btn_4.grid(row = 1, column = 0, sticky = tk.W + tk.E)

    btn_5 = tk.Button(button_frame, text = 'Exit program', font = ('Ariel', 16))
    btn_5.grid(row = 1, column = 2, sticky = tk.W + tk.E)

    button_frame.pack(padx = 10, pady = 30)


    # Run this bad boy
    window.mainloop()


########## Show lists of meals window ##########
'''def list_meals():
    window = tk.Tk()
    window.geometry('900x600')
    window.title('List Meals')
    welcome = tk.Label(window, text = 'List Meals', font = ('Ariel', 18))
    welcome.pack(padx = 20, pady = 20)


     # Find meal choice buttons
    operation_prompt = tk.Label(window, text = 'What level of recipes do you want to take a look at?', font = ('Ariel', 14))
    operation_prompt.pack(padx = 20, pady = 20)

    button_frame = tk.Frame(window)
    button_frame.columnconfigure(0, weight = 1)
    button_frame.columnconfigure(1, weight = 1)
    button_frame.columnconfigure(2, weight = 0)

    btn_1 = tk.Button(button_frame, text = 'Easy meals', font = ('Ariel', 16))
    btn_1.grid(row = 0, column = 0, sticky = tk.W + tk.E)

    btn_2 = tk.Button(button_frame, text = 'Medium meals', font = ('Ariel', 16))
    btn_2.grid(row = 0, column = 1, sticky = tk.W + tk.E)

    btn_3 = tk.Button(button_frame, text = 'Ambitious meals', font = ('Ariel', 16))
    btn_3.grid(row = 0, column = 2, sticky = tk.W + tk.E)

    btn_4 = tk.Button(button_frame, text = 'Back to main menu', font = ('Ariel', 16))
    btn_4.grid(row = 1, column = 0, sticky = tk.W + tk.E)

    btn_5 = tk.Button(button_frame, text = 'Exit program', font = ('Ariel', 16))
    btn_5.grid(row = 1, column = 1, sticky = tk.W + tk.E)

    button_frame.pack(padx = 10, pady = 30)


    # Run this bad boy
    window.mainloop()


########## Add a new meal window ##########
def add_meal():
    window = tk.Tk()
    window.geometry('900x600')
    window.title('Add Recipes')
    welcome = tk.Label(window, text = 'Add Recipes', font = ('Ariel', 18))
    welcome.pack(padx = 20, pady = 20)


     # Find meal choice buttons
    operation_prompt = tk.Label(window, text = 'What level of ambition is the recipe you want to add?', font = ('Ariel', 14))
    operation_prompt.pack(padx = 20, pady = 20)

    button_frame = tk.Frame(window)
    button_frame.columnconfigure(0, weight = 1)
    button_frame.columnconfigure(1, weight = 1)
    button_frame.columnconfigure(2, weight = 0)

    btn_1 = tk.Button(button_frame, text = 'Easy meal', font = ('Ariel', 16))
    btn_1.grid(row = 0, column = 0, sticky = tk.W + tk.E)

    btn_2 = tk.Button(button_frame, text = 'Medium meal', font = ('Ariel', 16))
    btn_2.grid(row = 0, column = 1, sticky = tk.W + tk.E)

    btn_3 = tk.Button(button_frame, text = 'Ambitious meal', font = ('Ariel', 16))
    btn_3.grid(row = 0, column = 2, sticky = tk.W + tk.E)

    btn_4 = tk.Button(button_frame, text = 'Back to main menu', font = ('Ariel', 16))
    btn_4.grid(row = 1, column = 0, sticky = tk.W + tk.E)

    btn_5 = tk.Button(button_frame, text = 'Exit program', font = ('Ariel', 16))
    btn_5.grid(row = 1, column = 1, sticky = tk.W + tk.E)

    button_frame.pack(padx = 10, pady = 30)


    # Run this bad boy
    window.mainloop()


########## Exit ##########
def close_program():
    exit
'''

########## Initiate program ##########
main_menu()