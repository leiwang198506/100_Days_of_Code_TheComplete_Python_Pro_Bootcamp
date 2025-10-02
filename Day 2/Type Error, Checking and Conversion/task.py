#functions
print(len("12345"))

#how to check the data type?
print(type("Hello"))
print(type(123))
print(type(123.4556565656))
print(type(True))

#type casting: convert data type, int(), float(), str(), bool()
int("123")
print(int("123")+int("456"))
#trun strings to numbers, ERROR!
#print(int("abc")+int("efg"))

#fix a code, turn integer to strings
print("Number of letters in your name: " + str(len(input("Enter your name"))))
