import random

numbers = list(range(1,101))

def easy_hard(guess_num,computer_choice):
    if guess_num<computer_choice:
        print("Too low")
    else:
        print("Too high")


print("Welcome to Number Guessing game")
print("I'm thinking a number between 1 and 100")

comp_choice = random.choice(numbers)
print(comp_choice)

first_choice = input("Choose your difficulty, easy or hard: ").lower()

if first_choice=="easy":
    print("You will have 10 attempts")
    i=0
    while i<=9:
        user_guess = int(input("Enter your guess: "))
        if user_guess!=comp_choice:
            easy_hard(user_guess,comp_choice)
            print(f"You have {9-i} attempts remaining")
            i += 1
        else:
            print("Congratulations you guessed it!")
            break

elif first_choice=="hard":
    print("You will have 5 attempts")
    i = 0
    while i <= 4:
        user_guess = int(input("Enter your guess: "))
        if user_guess != comp_choice:
            easy_hard(user_guess,comp_choice)
            print(f"You have {4 - i} attempts remaining")
            i += 1
        else:
            print("Congratulations you guessed it!")
            break

