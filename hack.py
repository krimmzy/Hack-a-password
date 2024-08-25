# Get the 4-digit number from the user
target_number = int(input("Enter a 4-digit number: "))

# Initialize the starting number
current_number = 0000  # Starting with the smallest 4-digit number

# Loop until the current number equals the target number
while current_number != target_number:
    print(f"Trying {current_number}...")
    current_number += 1

print(f"Found the number: {current_number}!")
