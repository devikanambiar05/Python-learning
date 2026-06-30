rock = '''
rock
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
paper
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
scissors
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random

print("Welcome to a game of rock, paper, scissors!")
trial = input("For rock type 0, for paper 1 and for scissors 2\n")

if trial == 0:

    print(rock)
elif trial == 1:

    print(paper)
else:
    print(scissors)

output = random.choice([rock, paper, scissors])
print("The computer chose: ")
print(output)

if trial == 0 and output == rock:
    print("It's a tie!")
elif trial == 1 and output == paper:
    print("It's a tie!")
elif trial == 2 and output == scissors:
        print("It's a tie!")
elif trial == 0 and output == paper:
    print("You lose :(")
elif trial == 0 and output == scissors:
    print("You win!")
elif trial == 1 and output == rock:
    print("You win!")
elif trial == 1 and output == scissors:
    print("You lose!")
elif trial == 2 and output == rock:
    print("You lose!")
else:
    print("You win!")