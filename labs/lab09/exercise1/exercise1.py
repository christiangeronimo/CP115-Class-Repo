# Student Classification System
# Get student information
student_name = input("Enter student name: ")
gpa = float(input("Enter GPA (0.0-4.0): "))
credit_hours = int(input("Enter credit hours: "))

# TODO your code here
# if statement - always at the beginning
student_grade = 85

if student_grade >= 90:
    print("Excellent performance")
    
percentage = (marks / total_marks) * 100
print(f"Student scored: {percentage}%")
# Display results
print(f"\nStudent: {student_name}")
print(f"GPA: {gpa}")
print(f"Credit Hours: {credit_hours}")
#print(f"Classification: {classification}")