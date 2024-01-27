"""
GRADE SORTER APP

This is a Python program that will collect four grades from a user. The program will then sort these grades from highest to lowest. Then, the program will simulate dropping the lowest two grades the user entered. Lastly, it will comment on the users highest grade.
"""

print("Welcome to the Grade Sorter Program!")

# Initialize list and get user input
grades = []
grades.append(int(input("What is your first grade (0-100): ")))
grades.append(int(input("What is your second grade (0-100): ")))
grades.append(int(input("What is your third grade (0-100): ")))
grades.append(int(input("What is your fourth grade (0-100): ")))

# Display user's grades
print("\nYour grades are: " + str(grades))

# Sort the list from highest to lowest
grades.sort(reverse=True)
print("\nYour grades from highest to lowest are: " + str(grades))

# Removing the lowest two grades
print("\nThe lowest two grades will now be dropped.")
removed_grade = grades.pop()
print("Removed grade: " + str(removed_grade))
removed_grade = grades.pop()
print("Removed grade: " + str(removed_grade))

# Recap remaining grades
print("\nYour remaining grades are: " + str(grades))
print("Nice work! Your highest grade is " + str(grades[0]) + ".")