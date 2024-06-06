import random

def phase1(user_choice, prob):
    randint = random.random()

    if randint < prob:
        if user_choice == "batu":
            computer_choice = "kertas"
        elif user_choice == "kertas":
            computer_choice = "gunting"
        else:
            computer_choice = "batu"
    else:
        computer_choice = random.choice(["batu", "kertas", "gunting"])

    return computer_choice