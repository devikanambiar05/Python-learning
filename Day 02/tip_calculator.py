#Let's make a tip calculator

food = int(input("How much did the food cost?\n"))
tip = int(input("How much percentage of tip do you want to give?(Directly write the number)\n"))
calc = (tip/100)*food
people = int(input("Among how many people do you want to divide the tip?\n"))
final = calc/people
ans = round(final,2)
print(f"Everyone has to pay {ans} each")