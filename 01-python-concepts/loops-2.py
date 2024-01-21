"""
ODD/EVEN NUMBER SORTER PROGRAM
This Python program sorts a list of comma-separated numbers as either even or odd. Upon sorting the numbers into two groups, the program will then sort each
group numerically and display the results. The program will continue to ask for the list of numbers unless the user states that they want to exit.
"""

print("Odd/Even Number Sorter Program")

while True:
    # Prompt user for a list of comma-separated numbers
    numbers_input = input("Enter a list of comma-separated numbers (e.g., 2,5,8,3): ")

    # Split the input into a list of numbers
    numbers = []
    for num in numbers_input.split(','):
        numbers.append(int(num))

    # Separate numbers into even and odd groups
    even_numbers = []
    odd_numbers = []

    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)
        else:
            odd_numbers.append(num)

    # Sort even and odd groups numerically
    even_numbers.sort()
    odd_numbers.sort()

    # Display the results
    print(f"\nSorted Even Numbers: {even_numbers}")
    print(f"Sorted Odd Numbers: {odd_numbers}")

    # Ask if the user wants to continue or exit
    user_choice = input("\nDo you want to enter another list? (yes/no): ")
    
    if user_choice.lower() != 'yes':
        print("Exiting the program. Thank you for using!")
        break

