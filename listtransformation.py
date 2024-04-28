#task1 
grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
grades.sort(reverse=True)
print(grades)

#task2
grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
total_grades = sum(grades)
num_grades = len(grades)
average_grade = total_grades / num_grades 
print("Average grade:", average_grade)

#task3
grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
grades = ["Failed" if grade < 80 else grade for grade in grades]
print(grades)