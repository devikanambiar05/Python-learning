logo = r'''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

user_name = input("What is your name?")
price = int(input("What is your bidding price?"))

dict = {
    "bidder":[user_name],
    "price":[price]
}

game = True
while game == True:

    another = input("Is there another bidder? Type 'yes' or 'no'").lower()

    if another=="yes":
            print("\n"*50)
            user_name = input("What is your name?")
            price = int(input("What is your bidding price?"))
            dict["bidder"].append(user_name)
            dict["price"].append(price)
    else:
        game = False

        print(dict)
        maxi = max(dict["price"])
        print(maxi)
        index_max = dict["price"].index(maxi)
        print(index_max)
        max_bidder = dict["bidder"][index_max]
        print(f"Congratulations to {max_bidder} with the highest bid of {maxi}")
