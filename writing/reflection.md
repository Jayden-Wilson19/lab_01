# Lab 01 Reflection

**Student Name:** Jayden Wilson  
**Date:** 1/28/2026

---

## Instructions

Now that you are completed all six programs, take some time to reflect on what you learned. Answer each question thoughtfully and in complete sentences. These questions are designed to help you think conceptually about loops and programming, not just recall code syntax. Please use clear and meaningful language in your responses --no one-liners or single-word answers, please!

---

## Conceptual Questions

### Question 1: For Loops vs While Loops

In your own words, explain the main difference between a `for` loop and a `while` loop. When would you choose to use one over the other? Provide an example scenario for each.

**Your Answer:**

Looking through each program, I can say that for loops are mainly used in connection with range, either with numbers or words. It will ask for an amount of said numbers or chracters in a list or word and later display the selected ones. For while loops, they take into consideration of whats given to them and will expand on it in some way or another. Unlike the for loop, while loops will leave whats given to them alone without asking to take and select certain information from it and instead will take it and make it bigger or smaller.

---

### Question 2: The Range Function

You used the `range()` function extensively in Program 1. Explain what `range(1, 10)`, `range(0, 20, 2)`, and `range(10, 0, -1)` each do. Why is the stop value "exclusive" (not included in the range)?

**Your Answer:**

The ranges being connected with the for loops in program 1 is a function that will allow you to enter numbers in that range for it to output the numbers in that range. For example, in the first program we were told to type range(1, 11), this will confuse many leaving people to believe that this range will display numbers from 1 - 11. Instead it will go form 1 - 10.

---

### Question 3: String Iteration

In Program 2, you looped through a string character by character. Explain why we can iterate over strings using a `for` loop. What does this tell you about how Python treats strings?

**Your Answer:**

In program 2, in our for loop(s) there was another function connected to it that allowed it to ignore the string and take the words and break it down as much as we wanted, the function being "char". Char is a function that is able to break through a string message allowing anything affiliated with it to also have acess to that string.

---

### Question 4: Nested Loops

Program 4 used nested loops to create patterns. Describe what happens when you have a loop inside another loop. How many times does the inner loop execute compared to the outer loop? Use an example from Program 4 to explain.

**Your Answer:**

For every iteration, the inner loop wil continue. The inner loop will continue to multiply its variables with the outer loops for each iteration until finished. In program 4, we assigned 5 to rows and 8 to cols. In the nested loop, the outer loop is assigned the rows and the inner is cols. After writing the nested loop it's shown that there is a print statement tells the inner loop to multiply both until the final print which will be the final output.

---

### Question 5: Loop Control and Break Statements

In Program 3, you used a `break` statement in the password checker. Explain what the `break` statement does and why it's useful. Can you think of another scenario where using `break` would be helpful?

**Your Answer:**

A break statement stops the loop it is connected to, skipping to the next statement. Another way break is used is when iterating through thousands of product IDs and finding a specific match. Once it's found, you can use a break to stop the search immediately. Breaks are really good when you want an easy way to stop your loops from not being continuous unless necessary

---

### Question 6: Accumulator Pattern

Several programs used the "accumulator pattern" where you initialize a variable to 0 (or an empty string/list) and then add to it inside a loop. Why is this pattern so important in programming? Give at least two examples from the lab where you used this pattern.

**Your Answer:**

TODO: Write your answer here (4-6 sentences)

---

### Question 7: Lists vs Dictionaries

Both Program 5 and Program 6 involved iterating over collections, but lists and dictionaries are different. Explain the key difference between how you loop through a list versus a dictionary. What methods did you use for dictionary iteration?

**Your Answer:**

TODO: Write your answer here (3-5 sentences)

---

### Question 8: The Enumerate Function

You used `enumerate()` in Programs 2 and 5 to get both the index and the value while looping. Explain what `enumerate()` does and why it's more convenient than manually tracking an index with a counter variable.

**Your Answer:**

TODO: Write your answer here (3-4 sentences)

---

### Question 9: Real-World Applications

Think about real-world problems or situations where loops would be essential. Describe at least two specific examples of how loops could be used in everyday programs or applications (not from this lab).

**Your Answer:**

Loops are a really important function that larger programming languages and places still use quite a bit. For loops are very useful when needing an easier way to look through a list of information and assign it to its respective position.



---

### Question 10: Debugging Loops

What was the most challenging bug or error you encountered while working on this lab? How did you figure out what was wrong? What debugging strategies did you use?

**Your Answer:**

For some of the programs, when running my code the output would display nothing as opposed to the information I had written down. Assuming it was due to not popping out in someway I tried looking for ways it could so it can display like the other information indentical to yours.

---

## Lab Feedback

### Feedback Question 1: Lab Difficulty

How would you rate the difficulty of this lab? Were the programs appropriately challenging, too easy, or too difficult? Which program was the most challenging and why?

**Your Answer:**

Being introduced to different loops for my first CMPSC course, this lab was fairly simple. In some cases, it was a nice refresher and a nice way for us to become familiar with these functions again.

---

### Feedback Question 2: Lab Improvements

What suggestions do you have for improving this lab? Was anything unclear in the instructions? Were the hints helpful? What would have made this lab better for your learning?

**Your Answer:**

Seeing as this lab was i'm assuming a great way to bring back our memories of loops, there isn't really much I would add or change. I think this lab served as a nice refresher for one of the most commonly used function in CMPSC. 

---

## Completion Checklist

Before submitting, make sure you have:

- [X] Completed all six programs in the `src/` folder
- [X] Tested each program and verified it produces the expected output
- [ ] Answered all 10 conceptual questions above
- [X] Answered both feedback questions
- [X] Added your name and date at the top of this document
- [ ] Reviewed your answers for completeness and clarity
- [ ] Committed and pushed all changes to GitHub

---

**Congratulations on completing Lab 01!** 🎉

you are taken an important step in mastering Python loops. The skills you are learned here will be fundamental to everything else you do in programming. Keep up the great work!
