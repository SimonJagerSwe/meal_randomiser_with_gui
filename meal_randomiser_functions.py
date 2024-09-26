########## Imports  ##########
import random


########## Lists ##########
easy_list = []
medium_list = []
ambitious_list = []


########## Functions for finding meals ##########
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


########## Functions for displaying meal lists ##########
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


########## Functions for adding new recipes ##########
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