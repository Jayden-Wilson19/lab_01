#!/usr/bin/env python3
"""

Name: Jayden Wilson

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
    for student, grade in student_grades.items():
        print(f"{student}: {grade}")
    # Print each student's name and grade
    # Hint: Use .items() method to get both key and value
    # Format: "Alice: 92"
    
    
    # STEP 2: Calculate class statistics
    print("\nClass Statistics:")
    total_students = len(student_grades)
    total_grade = sum(student_grades.values())
    average_grade = total_grade / total_students
    highest_grade = max(student_grades.values())
    lowest_grade = min(student_grades.values())
    # - Total number of students
    # - Average grade
    # - Highest grade
    # - Lowest grade
    
    
    # STEP 3: Grade categorization
    print("\nGrade Categories:")
    for student, grade in student_grades.items():
        if grade >= 90:
            category = 'A'
        elif grade >= 80:
            category = 'B'
        elif grade >= 70:
            category = 'C'
        elif grade >= 60:
            category = 'D'
        else:
            category = 'F'
        print(f"{student}: {grade} ({category})")
    # A (90-100), B (80-89), C (70-79), D (60-69), F (below 60)
    # Hint: Use conditionals inside your loop
    
    
    # STEP 4: Find students above average
    print("\nStudents scoring above average:")
    for student, grade in student_grades.items():
        if grade > average_grade:
            print(f"{student}: {grade}")
    # Print names of students whose grades are above average
    
    
    # STEP 5: Inventory report
    print("\nStore Inventory Report:")
    print("-" * 30)
    for item, quantity in inventory.items():
        print(f"{item}: {quantity} in stock")
    # Print each item and its quantity
    # Format: "apples: 45 in stock"
    
    
    # STEP 6: Low stock alert
    print("\nLow Stock Alert (less than 20 items):")
    for item, quantity in inventory.items():
        if quantity < 20:
            print(f"Alert: {item} has only {quantity} units left!")
    # Print items that have less than 20 units in stock
    
    
    # STEP 7: Total inventory count
    print("\nTotal Inventory:")
    total_items = sum(inventory.values())
    print(f"Total items in inventory: {total_items}")
    # across all products
    
    
    print("\n" + "=" * 50)
    print("Program 6 Complete!")
    print("=" * 50)


if __name__ == "__main__":
    main()
