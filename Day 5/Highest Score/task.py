student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
# print(range(1, 10))
total_exam_score= sum(student_scores)
print(total_exam_score)

#find sum of the values
sum=0
for score in student_scores:
    sum+=score
print(sum)


#find max of the values
#method1:
print(max(student_scores))
#method2: use for loop
temp_value=student_scores[0]
for score in student_scores:
    if score >temp_value:
        temp_value=score
print(temp_value)