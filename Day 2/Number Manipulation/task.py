
bmi = 84 / 1.65 ** 2
print(bmi) #lots of numbers after decimal

#round number round()
print(round(bmi))
round(bmi,2)
print(round(bmi,2))


#Assignment Operators
score=0
score+=1
print(score)
height=1.65
is_win= True

#f-Strings
print("Your score is " + str(score)) #have to convert score to string, painful!!
print(f"your score is {score}, your height is {height} and you are winning is {is_win}")
