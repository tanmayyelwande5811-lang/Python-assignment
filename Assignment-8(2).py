from student_package.student_info import display_student
from student_package.result import (
    calculate_total,
    calculate_percentage,
    calculate_grade,
)

# display all info
display_student("Tanmay Yelwande", 34, "AI & ML")

marks = [80, 78, 96, 89, 70]

total = calculate_total(marks)
percentage = calculate_percentage(marks)
grade = calculate_grade(percentage)

print("\nStudent Result")
print("Total marks:", total)
print("Percentage:", percentage)
print("Grade:", grade)