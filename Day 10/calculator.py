def add(a,b):
    return a+b

def subtract(a,b):
    return a-b


def multiply(a,b):
    return a*b

def division(a,b):
    return a/b

def calculator(first,second,third):
    if operation == "+":
        ans = add(first,third)
    elif operation == "-":
        ans = subtract(first,third)
    elif operation == "*":
        ans = multiply(first,third)
    elif operation == "/":
        ans = division(first,third)

    return ans

n1 = int(input("Enter first number: "))
operation = input("Enter mathematical operation\n+\n-\n*\n/\n")
n2 = int(input("Enter second number: "))

final_ans = calculator(n1,operation,n2)
print(f"{n1} {operation} {n2} = {final_ans}")

game = True

while game:
    choice = input("Do you wish to continue with the answer as the first number?'yes' or 'no'").lower()
    if choice =="yes":
        operation = input("Enter mathematical operation\n+\n-\n*\n/\n")
        n2 = int(input("Enter second number: "))
        next_ans = calculator(final_ans,operation,n2)
        print(f"{final_ans} {operation} {n2} = {next_ans}")
        final_ans = next_ans
    else:
        print("\n"*50)
        n1 = int(input("Enter first number: "))
        operation = input("Enter mathematical operation\n+\n-\n*\n/\n")
        n2 = int(input("Enter second number: "))
        final_ans = calculator(n1, operation, n2)
        print(f"{n1} {operation} {n2} = {final_ans}")



