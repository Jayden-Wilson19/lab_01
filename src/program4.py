#!/usr/bin/env python3
"""

Name: Jayden Wilson

Program 4: Nested Loops and Patterns
This program uses nested loops to create visual patterns.
Here, we learn how inner and outer loops work together.
"""

def main():
    """
    Main function to demonstrate nested loops.
    """
    
    print("=" * 50)
    print("Program 4: Nested Loops and Patterns")
    print("=" * 50)
    
    # STEP 1: Create a simple rectangle of stars
    # Make a 5 rows by 8 columns rectangle
    print("\nPattern 1: Rectangle (5x8)")
    rows = 5
    cols = 8
    for i in range(rows):
        for j in range(cols):
            print("*", end="")
        print()
    # Outer loop: iterate over rows
    # Inner loop: iterate over columns
    # Hint: Use print("*", end="") to print without newline
    # Use print() after inner loop to move to next line
    
    
    # STEP 2: Create a right triangle
    # Row 1: *
    # Row 2: **
    # Row 3: ***
    # Row 4: ****
    # Row 5: *****
    print("\nPattern 2: Right Triangle")
    height = 5
    for row in range(1, height + 1):
        for star in range(row):
            print("*", end="")
        print()
    # Hint: If outer loop is row (1 to 5), inner loop should print 'row' stars
    
    
    # STEP 3: Create a multiplication table (1-5)
    print("\nPattern 3: Multiplication Table (1-5)")
    print("   ", end="")
    # Print header row
    for i in range(1, 6):
        print(f"{i:4}", end="")
    print()
    print("   " + "-" * 20)
    
    for i in range(1, 6):
        print(f"{i}|", end="")
        for j in range(1, 6):
            product = i * j
            print(f"{product:4}", end="")
        print()
    # Outer loop: rows (1 to 5)
    # Inner loop: columns (1 to 5)
    # Print row number, then calculate and print each product
    # Hint: Use formatting like print(f"{product:4}", end="") to align columns
    
    
    # STEP 4: Number pyramid
    # Row 1:     1
    # Row 2:    121
    # Row 3:   12321
    # Row 4:  1234321
    print("\nPattern 4: Number Pyramid")
    pyramid_height = 4
    for row in range(1, pyramid_height + 1):
        # Print leading spaces
        for space in range(pyramid_height - row):
            print(" ", end="")
        # Print ascending numbers
        for num in range(1, row + 1):
            print(num, end="")
        # Print descending numbers
        for num in range(row - 1, 0, -1):
            print(num, end="")
        print()
    # This is challenging! You'll need:
    # - Outer loop for rows
    # - Loop to print leading spaces
    # - Loop to print ascending numbers
    # - Loop to print descending numbers
    
    
    print("\n" + "=" * 50)
    print("Program 4 Complete!")
    print("=" * 50)


if __name__ == "__main__":
    main()
