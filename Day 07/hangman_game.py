stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

import random

word_list = ["aardvark", "baboon", "camel"]

print("Welcome to Hangman!")

#computer chooses a random word and displays the dashes

chosen_word = random.choice(word_list)
length = len(chosen_word)

placeholder = ""
for i in range(length):
    placeholder += "_"

print("Your unknown word is:\n" + placeholder)

#you take the person's guess
game_over = False
remember = ""
lives = 7
k=6
while not game_over:
    guess = input("Enter your guess: ").lower()

    final = ""

    for i in chosen_word:
        if i == guess:
            final += i
            remember += i
        elif i in remember:
            final += i
        else:
            final += "_"

    print(final)


    if guess not in chosen_word:
        lives-=1
        print(stages[k])
        k -= 1


    if "_" not in final:
        game_over = True
        print("You win!")

    if lives == 0:
        game_over = True
        print("Game over\nYou lose :(")



