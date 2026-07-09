logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""
condition = 2
print(logo)
print("Welcome to Caeser Cipher!")
while condition != 0:
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    def encrypt(original_text,shift_amount):
        new_letter = ""
        for i in original_text: #abc a
            if i != " ":

                index = alphabet.index(i)
                new_index = index + shift_amount

                if new_index > 25:
                    new_new_index = new_index-index
                    new_letter += alphabet[new_new_index-1]

                else:
                    new_letter += alphabet[new_index]

            else:
                new_letter += ""


        print(f"Your encoded message is {new_letter}")

    def decrypt(original_text,shift_amount):
        new_letter = ""
        for i in original_text:  # abc a
            if i != " ":
                index = alphabet.index(i)
                new_index = index - shift_amount

                if new_index < 0:
                    abs_value = 26-abs(new_index)
                    new_letter += alphabet[abs_value]

                else:
                    new_letter += alphabet[new_index]

            else:
                new_letter += ""

        print(f"Your decoded message is {new_letter}")
    if direction=="encode":
        encrypt(text,shift)
    elif direction == "decode":
        decrypt(text,shift)
    else:
        print("Please type either 'encode' or 'decode'")

    condition-=1