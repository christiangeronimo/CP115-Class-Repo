grade1 = 78 
grade2 = 85
grade3 = 92
grade4 = 67
grade5 = 88
percentage = 100
total_score = (grade1 + grade2 + grade3 + grade4 + grade5)


average_point = total_score // 5
percentage_grade1 = (grade1/total_score)*percentage
percentage_grade2 = (grade2/total_score)*percentage
percentage_grade3 = (grade3/total_score)*percentage
percentage_grade4 = (grade4/total_score)*percentage
percentage_grade5 = (grade5/total_score)*percentage

print(f"GRADE 1 : {grade1}")
print(f"GRADE 2 : {grade2}")
print(f"GRADE 3 : {grade3}")
print(f"GRADE 4 : {grade4}")
print(f"GRADE 5 : {grade5}")

print(f"AVERAGE : {average_point}")
print(f"Percentage Contribute Grade 1 : {percentage_grade1}")
print(f"Percentage Contribute Grade 2 : {percentage_grade2}")
print(f"Percentage Contribute Grade 3 : {percentage_grade3}")
print(f"Percentage Contribute Grade 4 : {percentage_grade4}")
print(f"Percentage Contribute Grade 5 : {percentage_grade5}")