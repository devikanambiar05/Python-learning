print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

print("Welcome to Treasure Island\nYour mission is to find the treasure.\n")

direction = input("Do you want to go left or right?\nType 'left' or 'right': ")
if direction == "left":
    swim_wait = input("Good choice!\nThere is a suspicious looking lake in front of you\nDo you want to swim or wait?\nType 'swim' or 'wait': ")
    if swim_wait == "swim":
        print("You get attacked by trout:(\nGAME OVER")
    else:
        door = input("There are 3 doors in front of you\nRed, Blue and Yellow?\nType 'red' or 'blue' or 'yellow': ")
        if door == "red":
            print("You get burned by fire!!!\nGAME OVER")
        elif door == "blue":
            print("You get eaten by beasts!!!\nGAME OVER")
        elif door == "yellow":
            print("You have reached the treasure!!\nYOU WIN!!")
        else:
            print("Invalid input\nGAME OVER")
else:
    print("You fell into a volcanic pit, Ouch!!\nGAME OVER")
