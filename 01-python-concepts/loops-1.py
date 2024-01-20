"""
GRADE POINT AVERAGE (GPA) CALCULATOR PROGRAM

This Python program that will collect any number of grades from a user. The program will sort these grades numerically from highest to lowest and calculate the grade point average of the user. It will then ask for the average the user desires and calculate what the user must get on their next assignment to achieve this average. Lastly, the program will make a copy of the users grades and allow them to alter one of their previous grades to see how doing worse or better on an assignment would have changed their overall average.
"""
print("GPA Calculator Program")

# Get user's name
name = input("What's your name? ").title().strip()

# Collect grades from the user
grades = []
num_grades = int(input("How many grades would you like to enter? "))

for i in range(num_grades):
    grade = float(input(f"Enter grade {i + 1}: "))
    grades.append(grade)

# Sort grades numerically from highest to lowest
grades.sort(reverse=True)

# Calculate the grade point average
average = sum(grades) / num_grades

# Display the sorted grades and the calculated GPA
print(f"\nYour grades from highest to lowest are {grades}")
print(f"Grade Point Average (GPA): {average:.2f}\n")

# Print the grade summary
print(f"{name}'s Grade Summary:")
print(f"Total number of grades: {str(len(grades))}")
print(f"Highest grade: {str(max(grades))}")
print(f"Lowest grade: {str(min(grades))}")
print(f"Average: {average}")

# Ask for the desired average
desired_average = float(input("\nEnter the average grade you desire: "))

# Calculate the grade needed on the next assignment
next_grade_needed = (desired_average * (num_grades + 1)) - sum(grades)
print(f"Good luck, {name}!")
print(f"To achieve an average of {desired_average}, you need to get {next_grade_needed:.2f} on your next assignment.\n")

# Make a copy of the user's grades
copied_grades = grades.copy()

# Allow the user to alter one of their previous grades
grade_to_alter = int(input("Enter the index of the grade you want to alter (starting from 1): "))
new_grade = float(input(f"Enter the new grade for assignment {grade_to_alter}: "))

# Update the copied grades
copied_grades[grade_to_alter - 1] = new_grade

# Calculate the new GPA with the altered grade
new_average = sum(copied_grades) / num_grades
print(f"\nAltered Grades (with the new grade): {copied_grades}")
print(f"New Grade Point Average (GPA): {new_average:.2f}")

# Print the new grade summary
print(f"\n{name}'s New Grade Summary:")
print(f"Total number of grades: {str(len(copied_grades))}")
print(f"Highest grade: {str(max(copied_grades))}")
print(f"Lowest grade: {str(min(copied_grades))}")
print(f"Average: {round(new_average, 2)}")

#Print a summary on how the average changed
print(f"\nYour new average would be {round(new_average, 2)} compared to your real average of {round(average, 2)}.")
average_change = new_average - average
average_change = round(average_change, 2)
print(f"That is a change of {str(average_change)} point(s)!")