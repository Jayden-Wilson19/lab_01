#!/usr/bin/env python3
"""

Name: Add Your Name Here

Program 6: Dictionary Explorer with Loops
This program demonstrates looping through dictionaries.
The dictionary is provided. Here, we learn how to access and process its data.
"""

def main():
    """
    Main function to demonstrate dictionary iteration.
    """
    
    print("=" * 50)
    print("Program 6: Dictionary Explorer with Loops")
    print("=" * 50)
    
    # Pre-defined dictionary (provided for you)
    # This represents a simple grade book
    student_grades = {
        "Alice": 92,
        "Bob": 87,
        "Charlie": 78,
        "Diana": 95,
        "Eve": 83,
        "Frank": 88,
        "Grace": 91,
        "Henry": 76
    }
    
    # Another dictionary: inventory of a store
    inventory = {
        "apples": 45,
        "bananas": 32,
        "oranges": 28,
        "grapes": 15,
        "strawberries": 8
    }
    
    # STEP 1: Print all students and their grades
    print("\nStudent Grade Report:")
    print("-" * 30)
    # TODO: Loop through student_grades dictionary
    # Print each student's name and grade
    # Hint: Use .items() method to get both key and value
    # Format: "Alice: 92"
    
    
    # STEP 2: Calculate class statistics
    print("\nClass Statistics:")
    # TODO: Loop through the grades and calculate:
    # - Total number of students
    # - Average grade
    # - Highest grade
    # - Lowest grade
    
    
    # STEP 3: Grade categorization
    print("\nGrade Categories:")
    # TODO: Count how many students are in each category:
    # A (90-100), B (80-89), C (70-79), D (60-69), F (below 60)
    # Hint: Use conditionals inside your loop
    
    
    # STEP 4: Find students above average
    print("\nStudents scoring above average:")
    # TODO: First calculate the average, then loop again
    # Print names of students whose grades are above average
    
    
    # STEP 5: Inventory report
    print("\nStore Inventory Report:")
    print("-" * 30)
    # TODO: Loop through inventory dictionary
    # Print each item and its quantity
    # Format: "apples: 45 in stock"
    
    
    # STEP 6: Low stock alert
    print("\nLow Stock Alert (less than 20 items):")
    # TODO: Loop through inventory
    # Print items that have less than 20 units in stock
    
    
    # STEP 7: Total inventory count
    print("\nTotal Inventory:")
    # TODO: Calculate and print the total number of items
    # across all products
    
    
    print("\n" + "=" * 50)
    print("Program 6 Complete!")
    print("=" * 50)


if __name__ == "__main__":
    main()
