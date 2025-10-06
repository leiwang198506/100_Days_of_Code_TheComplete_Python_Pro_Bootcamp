from idlelib.pyshell import use_subprocess

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random
choices=[rock, paper, scissors]

#user choose and print out result
user_choice=int(input("Welcome to  Rock Paper Scissors Game! What do you choose? "
       "Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))
#print(user_choice)
if user_choice >= 0 and user_choice <= 2:
    print(choices[user_choice])
## #computer choose and print out results
    computer_choice=random.randint(0,2)
#print(f"Computer chose: {computer_choice}\n")
    print(choices[computer_choice])

#compare results
# print(user_choice-computer_choice)
    if (user_choice-computer_choice)== -2 or (user_choice-computer_choice)==1:
        print("Congratulation, you win! You are so smart!")
    elif user_choice == computer_choice:
        print("It's a draw! We are both so smart!")
    elif (user_choice - computer_choice) == -1 or (user_choice - computer_choice) == 2:
        print("You lose! Try again!")
else:
    print("Invalid number, you lose!")



# ###user	computer	substraction	result
# 0 1  -1	lose
# 1	2  -1	lose
# 2	0	2	lose
# 0	0	0	tie
# 1	1	0	tie
# 2	2	0	tie
# 0	2	-2	win
# 1	0	1	win
# 2	1	1	win
# o: rock
# 1: paper
# 2: scissor