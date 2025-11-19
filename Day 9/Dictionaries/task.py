# programming_dictionary = {
#     "Bug": "An error in a program that prevents the program from running as expected.",
#     "Function": "A piece of code that you can easily call over and over again.",
# }
#
# # print(programming_dictionary["Bug"])
# programming_dictionary["Loop"]="The atction of doing something over and over again."
#
#
#
# empty_dictionary={}
#
# empty_dictionary["1st item"]="This is the first item"
# # print(empty_dictionary)
# # programming_dictionary={}
# # print(programming_dictionary)
# # print(programming_dictionary["Bug"])
# programming_dictionary["Bug"]="This is the new bug"
# # print(programming_dictionary["Bug"])
#
# for key in programming_dictionary:
#     print(key)
#     print(programming_dictionary[key])


student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}
for key in student_scores:
    if 91 <= int(student_scores[key]) <= 100:
        student_grades[key] = "Outstanding"
    elif int(81 <= student_scores[key]) <= 90:
        student_grades[key] = "Exceeds Expectations"
    elif int(71 <= student_scores[key]) <= 80:
        student_grades[key] = "Acceptable"
    else:
        student_grades[key] = "Fail"

print(student_grades)
