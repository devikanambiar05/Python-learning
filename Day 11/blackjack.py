
import random

def win_predictor(player_sum,dealer_sum,player_card,dealer_card):
    if player_sum==dealer_sum:
        print("It's a DRAW")
    elif dealer_sum==21:
        print("You lose, DEALER WINS!")
    elif player_sum==21:
        print("YOU WIN!")
    elif player_sum>21:
        print("Your hand value is more than 21, BUST, YOU LOSE")
    elif dealer_sum>21:
        print("Dealer's hand value is more than 21, YOU WIN")
    elif player_sum>dealer_sum:
        print("YOU WIN")
    elif dealer_sum>player_sum:
        print("Dealer wins, YOU LOSE")


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
rand_player_card = []
rand_comp_card = []
game = True

while game:
    enter = input("Welcome to my Blackjack!!\n Type 'haha' to start").lower()


    if enter =="haha":
        rand_player_card = random.sample(cards,k=2)
        print(f"Your cards are : {rand_player_card}")
        rand_player_sum = sum(rand_player_card)
        print(f"The score is : {rand_player_sum}")

        rand_comp_card = random.sample(cards,k=1)
        print(f"The dealer's card is: {rand_comp_card}")
        print(f"The dealer's score is : {rand_comp_card[0]}")

        choice = input("If you want to get another card type 'y', if you wanna pass type 'n'")

        if choice == "y":
            rand_player_card += random.sample(cards,k=1)
            rand_player_sum = sum(rand_player_card)
            print(f"Your cards are : {rand_player_card}")
            print(f"The score is : {rand_player_sum}")

            rand_comp_card += random.sample(cards,k=1)
            rand_comp_sum = sum(rand_comp_card)
            print(f"The dealer's card is: {rand_comp_card}")
            print(f"The dealer's score is : {rand_comp_sum}")

            #dealer condition of having below 16
            win_predictor(rand_player_sum,rand_comp_sum,rand_player_card,rand_comp_card)

        else:
            rand_comp_card += random.sample(cards, k=1)
            rand_comp_sum = sum(rand_comp_card)
            print(f"The dealer's card is: {rand_comp_card}")
            print(f"The dealer's score is : {rand_comp_sum}")
            win_predictor(rand_player_sum, rand_comp_sum, rand_player_card, rand_comp_card)

        next_choice = input("Do you wanna play another game? Type 'yes' or 'no'")
        if next_choice == "yes":
            print("\n"*50)
            game = True
        else:
            game = False