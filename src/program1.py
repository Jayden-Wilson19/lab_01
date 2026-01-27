#!/usr/bin/env python3
"""

Name: Jayden Wilson

Program 1: Number Pattern Printer
This program uses a for loop with range() to print numbers in a specific pattern.
Here, we learn how to control loop iteration and format output.
"""

def main():
    """
    Main function to demonstrate basic for loops with range.
    """
    
    print("=" * 50)
    print("Program 1: Number Pattern Printer")
    print("=" * 50)
    
    # STEP 1: Print numbers from 1 to 10
    # Hint: Use range(start, stop) where stop is exclusive
    print("\nNumbers from 1 to 10:")
    for i in range(1, 11):
        print(i)
    
    
    # STEP 2: Print even numbers from 2 to 20
    # Hint: Use range(start, stop, step) with step=2
    print("\nEven numbers from 2 to 20:")
    for i in range(2, 21, 2):
        print(i)
    
    
    # STEP 3: Print numbers from 10 down to 1 (countdown)
    # Hint: Use a negative step in range()
    print("\nCountdown from 10 to 1:")
    for i in range(10, 0, -1):
        print(i)
    
    
    # STEP 4: Calculate and print the sum of numbers 1 to 100
    # Hint: Create a variable to accumulate the sum
    print("\nSum of numbers from 1 to 100:")
    sum_total = sum(range(1, 101))
    print(f"The sum is: {sum_total}")
    
    print("\n" + "=" * 50)
    print("Program 1 Complete!")
    print("=" * 50)


if __name__ == "__main__":
    main()
