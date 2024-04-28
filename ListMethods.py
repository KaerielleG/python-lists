#task1 
submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]
names = submitted + attended 
print(names)

#task2
submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]

submitted_sorted = sorted(submitted)
attended_sorted = sorted(attended)

if submitted_sorted == attended_sorted:
    print("The lists are identical in terms of their content, regardless of order.")
else: 
    print("The lists are not identical in terms of their content.")

#task3
submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]

attended_and_submitted = [student for student in attended if student in submitted]

print("Students who attended the class and submitted their assignment:", attended_and_submitted)
