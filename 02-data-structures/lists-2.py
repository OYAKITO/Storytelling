"""
GROCERY LIST PROGRAM
This Python program will simulate a grocery shopping list. The program will start with two items on the shopping list, meat and cheese, and then allow a user to add three new items to the list. To simulate shopping, the program will ask the user what item they just purchased and then remove the item from the shopping list. Upon having only two items in the shopping list, the program will inform the user that the store is out of a particular item and prompt the user to replace the item with a new item. You will use the datetime library to display the current date and time the shopping is taking place in mm/dd hh:mm format.
"""

import datetime

# Create the datetime object and store the current date and time
time = datetime.datetime.now()
formatted_time = time.strftime("%m/%d %H:%M")

# Welcome message and initial grocery list
foods = ["Meat", "Cheese"]
print("Welcome to the the Cloud Nine Superstore!")
print(f"Current Date and Time: {formatted_time}")
print(f"You currently have {', '.join(foods)} in your list.")

# Get user input to add three new items to the grocery list
for _ in range(3):
    food = input("\nType of food to add to the grocery list: ").title()
    foods.append(food)

# Print and sort the list
print("\nHere is your grocery list:")
print(foods)
foods.sort()
print("Here is your grocery list sorted:")
print(foods)

# Simulate Shopping
print("\nSimulating grocery shopping...")

# Iteratively ask the user what food they just bought and remove it from the list
for _ in range(3):
    print(f"\nCurrent grocery list: {len(foods)} items")
    print(foods)
    buy_food = input("What food did you just buy: ").title()

    if buy_food in foods:
        foods.remove(buy_food)
        print(f"Removing {buy_food} from the list...")

# The store is out of an item
print(f"\nCurrent grocery list: {len(foods)} items")
print(foods)
no_item = foods.pop()
print(f"\nSorry, the store is out of {no_item}.")
new_food = input("What food would you like instead: ").title()
foods.insert(0, new_food)

# Display the remaining grocery list
print("\nHere is what remains on your grocery list:")
print(foods)

