# # Functions with input
#
# def greet_with_name(name):
#     print(f"Hello {name}")
#     print(f"How do you do {name}?")
#
#
# greet_with_name("Jack Bauer")
#
#
# greet()
#
# def greet_with_name(name):
#     print(f"Hello {name}!")
#     print(f"How are you today {name}?")
#     print(f"Is everything ok {name}?")
# greet_with_name("HAHA")

# Functions with more than 1 input
def greet_with_name_and_place(name,place):
    print(f"Hello {name} from {place}!")
    print(f"How are you today {name} from {place}?")
    print(f"Is everything ok {name} from {place}?")
greet_with_name_and_place("lei","Montreal")

#postional argument, only check the position
greet_with_name_and_place("Montreal","Lei")

#keyword arguments
greet_with_name_and_place(place="Brossard", name="Lei")