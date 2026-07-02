import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to our password generator!")

user_letter = int(input("How many letters do you want in your password?\n"))
user_number = int(input("How many numbers do you want in your password?\n"))
user_symbol = int(input("How many symbols do you want in your password?\n"))

#easy way, without shuffle

password = ""

for i in range(0,user_letter):
    rand_letter = random.choice(letters)
    password += rand_letter

for i in range(0,user_number):
    rand_number = random.choice(numbers)
    password += rand_number

for i in range(0,user_symbol):
    rand_symbol = random.choice(symbols)
    password += rand_symbol

print(f"Your first password is: {password}")


#hard way, all the strings are shuffled

password2 = []

for i in range(0,user_letter):
    rand_letter = random.choice(letters)
    password2 += rand_letter

for i in range(0,user_number):
    rand_number = random.choice(numbers)
    password2 += rand_number

for i in range(0,user_symbol):
    rand_symbol = random.choice(symbols)
    password2 += rand_symbol

random.shuffle(password2)

password3 = ""

for i in password2:
    password3 += i

print(f"Your second password is: {password3}")






