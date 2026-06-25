
#password generator

print("Hello there....user....hmmm what should I call you?\n")
username = input("Enter your name: ")
print("Welcome " + username + "!\n")
print("Let's generate a password shall we!\n")
input("Type 'y' if your answer is yes\n")
print("Let's get into it!!!!")
pet_name = input("What's your pet name: \n")
month = input("Which month were you born: \n")
food = input("What's your favourite food: \n")
password = pet_name[0]+pet_name[1]+month[0]+month[1]+food[0]+food[1]
print("Your six letter password is: " + password)






