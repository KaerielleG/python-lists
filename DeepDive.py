#task1
students = ["John", "Doe", "Jane", "Smith"]
grades = [85, 90, 78, 88]
activities = ["Football", "Music", "Art", "Dance"]
# Use zip to iterate over all three lists simultaneously
for student, grade, activity in zip(students, grades, activities):
    if grade < 80:
        print(student, grade, activity)

#task2
students = ["John", "Doe", "Jane", "Smith"]
grades = [85, 90, 78, 88]
activities = ["Football", "Music", "Art", "Dance"]
students_approved = []
# Use zip to iterate over all three lists simultaneously
for student, grade, activity in zip(students, grades, activities):
    if grade >= 80:
        students_approved.append(student)
print("students_approved =", students_approved)

#task3
students_approved = ["John", "Doe", "Smith"]
print("students_approved =", students_approved)
