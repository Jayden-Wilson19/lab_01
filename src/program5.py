#!/usr/bin/env python3
"""

Name: Jayden Wilson

Program 5: List Processing with Loops
This program demonstrates looping through lists and using conditionals.
Lists are provided. Here, we learn how to process their contents.
"""

def main():
    """
    Main function to demonstrate list iteration.
    """
    
    print("=" * 50)
    print("Program 5: List Processing with Loops")
    print("=" * 50)
    
    # Pre-defined lists to work with (provided for you)
    numbers = [15, 42, 7, 23, 8, 16, 31, 4, 19, 12]
    names = ["Alice", "Bob", "Charlie", "Diana", "Eve", "Frank"]
    temperatures = [72, 68, 75, 80, 65, 71, 77, 82, 69, 73]
    
    # STEP 1: Print all numbers with their indices
    print("\nList of numbers with indices:")
    print(f"Original list: {numbers}")
    for index in range(len(numbers)):
        print(f"Index {index}: {numbers[index]}")
    # Format: "Index 0: 15"
    
    
    # STEP 2: Find and print all even numbers from the list
    print("\nEven numbers from the list:")
    for num in numbers:
        if num % 2 == 0:
            print(num)
    # Hint: Use the modulo operator (%) to check if a number is even
    
    
    # STEP 3: Calculate statistics
    print("\nNumber statistics:")
    total_sum = 0
    largest = numbers[0]
    smallest = numbers[0]
    # - The sum of all numbers
    # - The average (mean) of all numbers
    # - The largest number
    # - The smallest number
    # Hint: You can use Python's built-in max() and min() functions
    
    
    # STEP 4: Filter names by length
    print("\nNames with 5 or more characters:")
    for name in names:
        if len(name) >= 5:
            print(name)
    # Print only names that have 5 or more characters
    # Hint: Use len() function to get the length of each name
    
    
    # STEP 5: Temperature analysis
    print("\nTemperature analysis:")
    above_75 = 0
    below_70 = 0
    # - How many days were above 75 degrees
    # - How many days were below 70 degrees
    # - How many days were comfortable (70-75 inclusive)
    
    
    # STEP 6: Create a new list with modified values
    print("\nDoubled numbers:")
    doubled = []
    for num in numbers:
        doubled.append(num * 2)
    # where each number is doubled
    # Hint: Use .append() to add items to the doubled list
    
    print(f"Original: {numbers}")
    print(f"Doubled: {doubled}")
    
    print("\n" + "=" * 50)
    print("Program 5 Complete!")
    print("=" * 50)


if __name__ == "__main__":
    main()
