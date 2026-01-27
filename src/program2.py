#!/usr/bin/env python3
"""

Name: Jayden Wilson

Program 2: String Character Explorer
This program demonstrates looping through strings character by character.
Here, we learn how to access individual characters and analyze string content.
"""

def main():
    """
    Main function to demonstrate string iteration with loops.
    """
    
    print("=" * 50)
    print("Program 2: String Character Explorer")
    print("=" * 50)
    
    # Pre-defined string to work with
    message = "Python Programming is Fun!"
    
    # STEP 1: Print each character on a separate line
    # Hint: You can loop directly over a string using 'for char in string'
    print(f"\nOriginal message: {message}")
    print("\nEach character on a separate line:")
    for char in message:
        print(char)
    
    
    # STEP 2: Count how many vowels are in the message
    # Hint: Check if each character is in the string 'aeiouAEIOU'
    print("\nCounting vowels:")
    vowel_count = 0
    for char in message:
        if char in 'aeiouAEIOU':
            vowel_count += 1
    
    
    print(f"Number of vowels: {vowel_count}")
    
    # STEP 3: Print each character with its index position
    # Hint: Use enumerate() function to get both index and character
    print("\nCharacters with their positions:")
    for index, char in enumerate(message):
        print(f"Index {index}: {char}")
    
    
    # STEP 4: Create a new string with only the uppercase letters
    # Hint: Use the .isupper() method to check if a character is uppercase
    print("\nExtracting uppercase letters:")
    uppercase_only = ""
    for char in message:
        if char.isupper():
            uppercase_only += char
    
    
    print(f"Uppercase letters only: {uppercase_only}")
    
    print("\n" + "=" * 50)
    print("Program 2 Complete!")
    print("=" * 50)


if __name__ == "__main__":
    main()
