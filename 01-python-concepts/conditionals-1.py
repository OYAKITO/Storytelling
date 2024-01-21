"""
COIN TOSS PROGRAM
This Python program will simulate flipping a coin n number of times. The program will present the user with an option to see the result of each individual flip. The program will also inform the user any time the number of heads flipped is equal to the number of tails flipped. Upon completion of all flips, the program will provide a summary table that shows the number and percentage of each flip.
"""

import random

print("Coin Toss Program")

# Prompt user for the number of coin flips
n = int(input("Enter the number of times you want to flip the coin: "))

# Initialize counters for heads and tails
heads_count = 0
tails_count = 0

# Initialize a list to store individual flip results
flip_results = []

# Simulate coin flips
for _ in range(n):
    # Generate a random number (0 for tails, 1 for heads)
    flip_result = random.randint(0, 1)

    # Increment counters based on the flip result
    if flip_result == 0:
        tails_count += 1
    else:
        heads_count += 1

    # Store individual flip result
    flip_results.append("Heads" if flip_result == 1 else "Tails")

    # Inform the user if the number of heads equals the number of tails
    if heads_count == tails_count:
        print(f"Equal number of heads and tails after {heads_count + tails_count} flips!")

# Display individual flip results
print("\nIndividual Flip Results:")
for i, result in enumerate(flip_results, start=1):
    print(f"Flip {i}: {result}")

# Display summary table
print("\nSummary Table:")
print(f"Total Flips: {heads_count + tails_count}")
print(f"Heads: {heads_count} ({heads_count / (heads_count + tails_count) * 100:.2f}%)")
print(f"Tails: {tails_count} ({tails_count / (heads_count + tails_count) * 100:.2f}%)")
