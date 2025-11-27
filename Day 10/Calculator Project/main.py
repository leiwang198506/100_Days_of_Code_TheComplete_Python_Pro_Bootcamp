#add functions into the dictionary, with key = +-*/
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
# Program asks the user to type the first number.
# Program works out the result based on the chosen mathematical operator.
def calculator(n1,n2):
    result=operations[operation_choice](float(n1),float(n2))
    return result

# Program asks if the user wants to continue working with the previous result.
# If yes, program loops to use the previous result as the first number and then repeats the calculation process.
# Program asks the user to type a mathematical operator (a choice of "+", "-", "*" or "/")
first_number = input("What's the first number?:")
for key in operations:
    print(key)
operation_choice = input("Pick an operation:")
# Program asks the user to type the second number.
second_number = input("What's the next number?:")
output= calculator(first_number, second_number)
print(f"{float(first_number)} {operation_choice} {float(second_number)} = {output}")
should_continue = input(f"Type 'y' to continue calculating with {calculator(first_number, second_number)} or type 'n' to start a new calculation:")
while should_continue == "y":
    first_number= output
    for key in operations:
        print(key)
    operation_choice = input("Pick an operation:")
    second_number = input("What's the next number?:")
    output=calculator(first_number, second_number)
    print(f"{float(first_number)} {operation_choice} {float(second_number)} = {output}")
    if should_continue == "n":
        print("/n"*100)
        calculator(first_number, second_number)




    # If no, program asks the user for the fist number again and wipes all memory of previous calculations.
# Add the logo from art.py
