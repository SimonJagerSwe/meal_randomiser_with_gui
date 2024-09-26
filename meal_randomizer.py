import random

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


# Medium meal function
def read_medium():
    with open('medium_meals.txt', mode = 'r') as medium_meals:
        for meal in medium_meals:
            medium_list = meal.split(',')
            medium_list.append(meal)
        random_meal = random.choice(medium_list)
        print(random_meal.strip())


# Ambitous meal function
def read_ambitious():
    with open('ambitious_meals.txt', mode = 'r') as ambitious_meals:
        for meal in ambitious_meals:
            ambitious_list = meal.split(',')
            ambitious_list.append(meal)
        random_meal = random.choice(ambitious_list)
        print(random_meal.strip())


# Display easy meals
def display_easy():
    with open('easy_meals.txt', mode = 'r') as display_easy:
        print(display_easy.read())


# Display medium meals
def display_medium():
    with open('medium_meals.txt', mode = 'r') as display_medium:
        print(display_medium.read())


# Display ambitious meals
def display_ambitious():
    with open('ambitious_meals.txt', mode = 'r') as display_ambitious:
        print(display_ambitious.read())


# Display all meals
def display_all():
    with open('easy_meals.txt', mode = 'r') as display_easy:
        print('Easy:\n' + display_easy.read() + '\n')
    
    with open('medium_meals.txt', mode = 'r') as display_medium:
        print('Medium:\n' + display_medium.read() + '\n')

    with open('ambitious_meals.txt', mode = 'r') as display_ambitious:
        print('Ambitious:\n' + display_ambitious.read())
    

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
print('#' * 25)
print('#' * 25)
print('##' + (' ' * 21) + '##')
print('##    FOOD SELECTOR    ##')
print('##' + (' ' * 21) + '##')
print('#' * 25)
print('#' * 25 + '\n\n')
print('Do you want to:\n\n1. Find recipe\n2. Show recipes\n3. Add recipe\n4. Exit programn\n')


# User choice
print('Make your choice:\n')
choice = str(input())


# Chose meal level to read
if choice == '1':
    print('Chose your level of ambition:\n1. Easy\n2. Medium\n3. Ambitious\n')
    print('Make your choice:\n')
    level_choice = str(input())
    if level_choice == '1':
        read_easy()
    elif level_choice == '2':
        read_medium()
    elif level_choice == '3':
        read_ambitious()


# Show all meals
if choice == '2':
    print('Chose level to display:\n1. Easy\n2. Medium\n3. Ambitious\n4. All\n')
    print('Make your choice:\n')
    display_choice = str(input())

    if display_choice == '1':
        display_easy()

    if display_choice == '2':
        display_medium()

    if display_choice == '3':
        display_ambitious()

    if display_choice == '4':
        display_all()


# Chose meal level to write
if choice == '3':
    print('Chose your level of ambition:\n1. Easy\n2. Medium\n3. Ambitious\n')
    print('Make your choice:\n')
    new_recipe_level = str(input())


# Add new recipes
    if new_recipe_level == '1':
        add_easy()
 
    elif new_recipe_level == '2':
        add_medium()

    elif new_recipe_level == '3':
        add_ambitous()


# Exit program
if choice == '4':
    exit()