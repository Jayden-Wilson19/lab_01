#!/usr/bin/env python3
"""

Name: Add Your Name Here

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
    # TODO: Use enumerate() to print each number with its index
    # Format: "Index 0: 15"
    
    
    # STEP 2: Find and print all even numbers from the list
    print("\nEven numbers from the list:")
    # TODO: Loop through numbers and print only even numbers
    # Hint: Use the modulo operator (%) to check if a number is even
    
    
    # STEP 3: Calculate statistics
    print("\nNumber statistics:")
    # TODO: Calculate and print:
    # - The sum of all numbers
    # - The average (mean) of all numbers
    # - The largest number
    # - The smallest number
    # Hint: You can use Python's built-in max() and min() functions
    
    
    # STEP 4: Filter names by length
    print("\nNames with 5 or more characters:")
    # TODO: Loop through the names list
    # Print only names that have 5 or more characters
    # Hint: Use len() function to get the length of each name
    
    
    # STEP 5: Temperature analysis
    print("\nTemperature analysis:")
    # TODO: Loop through temperatures and count:
    # - How many days were above 75 degrees
    # - How many days were below 70 degrees
    # - How many days were comfortable (70-75 inclusive)
    
    
    # STEP 6: Create a new list with modified values
    print("\nDoubled numbers:")
    doubled = []
    # TODO: Loop through numbers and create a new list
    # where each number is doubled
    # Hint: Use .append() to add items to the doubled list
    
    print(f"Original: {numbers}")
    print(f"Doubled: {doubled}")
    
    print("\n" + "=" * 50)
    print("Program 5 Complete!")
    print("=" * 50)


if __name__ == "__main__":
    main()
