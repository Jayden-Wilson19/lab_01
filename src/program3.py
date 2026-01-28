#!/usr/bin/env python3
"""

Name: Jayden Wilson

Program 3: While Loop Adventure
This program demonstrates while loops with different conditions.
Here, we learn how while loops differ from for loops and when to use them.
"""

def main():
    """
    Main function to demonstrate while loops.
    """
    
    print("=" * 50)
    print("Program 3: While Loop Adventure")
    print("=" * 50)
    
    # STEP 1: Simple counter with while loop
    # Print numbers from 1 to 5 using a while loop
    print("\nCounting with while loop (1 to 5):")
    counter = 1
    while counter <= 5:
        print(counter)
        counter += 1
    # Hint: Don't forget to increment the counter!
    
    
    # STEP 2: Keep doubling until we exceed 1000
    # Start with 1 and keep doubling
    print("\nDoubling numbers until exceeding 1000:")
    number = 1
    while number <= 1000:
        print(number)
        number *= 2
    # Stop when number exceeds 1000
    
    
    # STEP 3: User input simulation (password checker)
    # We'll simulate checking a password with a limited number of attempts
    print("\nPassword checking simulation:")
    correct_password = "python123"
    attempts = 0
    max_attempts = 3
    
    # For this lab, we'll use pre-set attempts instead of input()
    # Simulate three wrong attempts, then the correct one
    test_passwords = ["wrong1", "wrong2", "wrong3", "python123"]
    
    while attempts < max_attempts:
        test_password = test_passwords[attempts]
        print(f"Attempt {attempts + 1}: Trying password '{test_password}'")
        if test_password == correct_password:
            print("Access Granted!")
            break
        else:
            print("Access Denied.")
        attempts += 1
    # Hint: Loop while attempts < max_attempts
    # Check if test_passwords[attempts] matches correct_password
    
    
    # STEP 4: Sum numbers until reaching a target
    print("\nAdding numbers until sum reaches 50:")
    total = 0
    current = 1
    while total < 50:
        total += current
        print(f"Added {current}, total is now {total}")
        current += 1
    # Stop when the total reaches or exceeds 50
    # Print each number being added and the running total
    
    
    print("\n" + "=" * 50)
    print("Program 3 Complete!")
    print("=" * 50)


if __name__ == "__main__":
    main()
