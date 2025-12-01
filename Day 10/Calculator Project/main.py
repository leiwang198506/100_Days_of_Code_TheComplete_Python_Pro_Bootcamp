#add functions into the dictionary, with key = +-*/
from operator import truediv


def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}
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
def calculator():
    print(logo)
    continue_calculate= True
    n1 = float(input("What's the first number?:"))
    while continue_calculate:
        for key in operations:
            print(key)
        operation_choice = input("Pick an operation:")
        n2 = float(input("What's the next number?:"))
        result=operations[operation_choice](n1,n2)
        print(f"{n1} {operation_choice} {n2} = {result}")
        choice = input(
            f"Type 'y' to continue calculating with {result} or type 'n' to start a new calculation:")
        if choice == "y":
            n1= result
        elif choice == "n":
            print("\n"*100)
            calculator()
        else:

            continue_calculate= False

calculator()