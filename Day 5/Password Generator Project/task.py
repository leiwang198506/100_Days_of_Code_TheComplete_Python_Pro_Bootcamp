import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#method 1: using random. choices()
# #get numbers
# pass_let= random.choices(letters,k=nr_letters)
# pass_symbol= random.choices(symbols,k=nr_symbols)
# pass_num=random.choices(numbers,k=nr_numbers)
#
# # #print out passwords in order
# password_list =pass_let + pass_symbol +pass_num
# #print(password_list)
#
# # # random everything together
# random_password_list = random.choices(password_list,k=nr_letters +nr_symbols+nr_numbers)
# #print(f"Your password is: {random_password_list}")
#
# #change list into strings
# password=""
# for char in random_password_list:
#     password+=char
# print(f"Your password is: {password}")
#

#method 2 easy mode: use random.choice and range(start_number, end_number)
#use strings
# #get numbers
# password=""
# for char in range(0, nr_letters):
#     password += random.choice(letters)
#
# for char in range(0, nr_symbols ):
#     password += random.choice(symbols)
#
# for char in range(0, nr_numbers):
#     password += random.choice(numbers)
#     print(password)
#

#method 2 hard mode: use random.choice and range(start_number, end_number)
#use list
#get numbers
password_list=[]
for char in range(0, nr_letters):
    password_list.append(random.choice(letters))
for char in range(0, nr_symbols ):
    password_list.append(random.choice(symbols))
for char in range(0, nr_numbers):
    password_list.append(random.choice(numbers))
print(password_list)

#change orders using random.shuffle
random.shuffle(password_list)
print(password_list)

#change list back to strings
password=""
for char in password_list:
    password+=char
print(f"Your password is: {password}")