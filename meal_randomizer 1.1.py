import random
from InquirerPy import inquirer

easy_list = []
medium_list = []
ambitious_list = []

# Easy meal function
def read_easy():
    with open('easy_meals.txt', mode = 'r') as easy_meals:       
        for meal in easy_meals:
            easy_list = meal.split(',')
            easy_list.append(meal)            
        random_meal = random.choice(easy_list)
        print(random_meal.strip())
        input()


# Medium meal function
def read_medium():
    with open('medium_meals.txt', mode = 'r') as medium_meals:
        for meal in medium_meals:
            medium_list = meal.split(',')
            medium_list.append(meal)
        random_meal = random.choice(medium_list)
        print(random_meal.strip())
        input()


# Ambitous meal function
def read_ambitious():
    with open('ambitious_meals.txt', mode = 'r') as ambitious_meals:
        for meal in ambitious_meals:
            ambitious_list = meal.split(',')
            ambitious_list.append(meal)
        random_meal = random.choice(ambitious_list)
        print(random_meal.strip())
        input()


# Display easy meals
def display_easy():
    with open('easy_meals.txt', mode = 'r') as display_easy:
        print(display_easy.read())
        input()


# Display medium meals
def display_medium():
    with open('medium_meals.txt', mode = 'r') as display_medium:
        print(display_medium.read())
        input()


# Display ambitious meals
def display_ambitious():
    with open('ambitious_meals.txt', mode = 'r') as display_ambitious:
        print(display_ambitious.read())
        input()


# Display all meals
def display_all():
    with open('easy_meals.txt', mode = 'r') as display_easy:
        print('Easy:\n' + display_easy.read() + '\n')
    
    with open('medium_meals.txt', mode = 'r') as display_medium:
        print('Medium:\n' + display_medium.read() + '\n')

    with open('ambitious_meals.txt', mode = 'r') as display_ambitious:
        print('Ambitious:\n' + display_ambitious.read())
    
    input()

# Add easy meal
def add_easy():
    with open('easy_meals.txt', mode = 'a') as easy_meals:        
        new_meal = easy_meals.write(', ' + input('Enter the name of the new meal: '))


# Add medium meal
def add_medium():
    with open('medium_meals.txt', mode = 'a') as medium_meals:
        new_meal = medium_meals.write(', ' + input('Enter the name of the new meal: '))


# Add ambitious meal
def add_ambitous():
    with open('ambitious_meals.txt', mode = 'a') as ambitious_meals:
        new_meal = ambitious_meals.write(', ' + input('Enter the name of the new meal: '))


# Main menu
print('\t\t' + '*' * 54)
print('\t\t' + '*' * 54)
print('\t\t' + '*' * 15 + ' ' * 24 + '*' * 15)
print('\t\t' + '*' * 12 + ' ' * 4 + 'MAGIC MEAL RANDOMIZER' + ' ' * 4, '*' * 12)
print('\t\t' + '*' * 15 + ' ' * 24 + '*' * 15)
print('\t\t' + '*' * 54)
print('\t\t' + '*' * 54)
choice = inquirer.select(
    message = '\nWhat do you want to do?\n',
    choices = ['Find a recipe', 'Show recipes', 'Add recipes', 'Exit']
    ).execute()


# Chose meal level to read
if choice == 'Find a recipe':
    level_choice = inquirer.select(
    message = 'How ambitious are you feeling?\n',
    choices = ['Easy', 'Medium', 'Ambitious']
    ).execute()
    if level_choice == 'Easy':
        read_easy()
    elif level_choice == 'Medium':
        read_medium()
    elif level_choice == 'Ambitious':
        read_ambitious()


# Show all meals
if choice == 'Show recipes':
    display_choice = inquirer.select(
    message = 'What level do you want to look at?\n',
    choices = ['Easy', 'Medium', 'Ambitious', 'All']
    ).execute()

    if display_choice == 'Easy':
        display_easy()

    if display_choice == 'Medium':
        display_medium()

    if display_choice == 'Ambitious':
        display_ambitious()

    if display_choice == 'All':
        display_all()


# Chose meal level to write
if choice == 'Add recipes':
    new_recipe_level = inquirer.select(
    message = 'How difficult is the recipe?\n',
    choices = ['Easy', 'Medium', 'Ambitious']
    ).execute()


# Add new recipes
    if new_recipe_level == 'Easy':
        add_easy()
 
    elif new_recipe_level == 'Medium':
        add_medium()

    elif new_recipe_level == 'Ambitious':
        add_ambitous()


# Exit program
if choice == 'Exit':
    exit()