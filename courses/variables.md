# Chapter 1: Variables and Data Types

In this chapter, we will explore the fundamental concepts of variables and data types in Python and compare them to what you are familiar with in C programming.

## Variables in Python

#### Variable Assignment

In Python, you can create variables without explicitly specifying their data types. This is quite different from C, where you must declare variables and specify their types. For example, in C, you might write:

```c
// C variable declaration
int number = 42;
```
In Python, it's much simpler:

```python
# Python variable assignment
number = 42
```

Dynamic Typing
Python uses dynamic typing, meaning a variable can change its data type during runtime. In C, once a variable is declared with a specific type, it can't change. Python's dynamic typing allows for more flexibility, but it also requires you to be mindful of the types your variables hold.

Common Data Types in Python
Python provides a range of data types, including:

Integers (int): Equivalent to C's int data type, but Python's integers have arbitrary precision.

Floating-Point Numbers (float): Comparable to C's float type, but Python handles floating-point arithmetic differently, often resulting in fewer precision issues.

Strings (str): Python's strings are similar to C's character arrays but much more versatile.

Lists and Tuples: Python offers two sequence types that are similar to arrays in C, but they can hold mixed data types and are more dynamic.

Data Type Conversion
In Python, you can easily convert between different data types using typecasting functions such as int(), float(), and str(). This flexibility contrasts with C, where explicit casting is often required.

```python
# Typecasting in Python
x = 42
y = float(x)  # Convert integer to float

# Typecasting in C
int x = 42;
float y = (float)x;  // Explicit casting required
```

Variable Naming Conventions
Python follows a different naming convention compared to C. Python uses snake_case for variable names (e.g., my_variable_name), while C typically uses camelCase (e.g., myVariableName) or underscores (e.g., myVariableName).

In this chapter, we have introduced Python's variable system and common data types, highlighting the differences and similarities with C. In the next chapter, we will explore control flow in Python and how it differs from C's control structures.



### [Control Flow](courses/control-flow.md)





















## Exercices

### Exercise 1: Swap Two Variables

Write a Python program that swaps the values of two variables without using a temporary variable. For example, if `x` is 5 and `y` is 10, after swapping, `x` should be 10 and `y` should be 5.

> Hint: See the code of this markdown file line 601.
<!-- You can use multiple assignment to swap two variables in Python. -->

### Exercise 2: Palindrome Checker

Create a Python function that checks whether a given string is a palindrome. A palindrome is a word, phrase, number, or other sequence that reads the same forward and backward (ignoring spaces, punctuation, and capitalization).

> Hint: See the code of this markdown file line 608.
<!-- You can use the `reversed()` function to reverse a string in Python. -->

### Exercise 3: Factorial Calculation

Write a Python program to calculate the factorial of a non-negative integer entered by the user. Ensure that the program handles input validation and provides the result.

> Hint: See the code of this markdown file line 615.
<!-- You can use recursion to calculate the factorial of a number in Python. -->

### Exercise 4: Fibonacci Sequence

Create a Python function that generates the Fibonacci sequence up to a specified number of terms. The Fibonacci sequence starts with 0 and 1, and each subsequent number is the sum of the two previous numbers.

> Hint: See the code of this markdown file line 622.
<!-- You can use recursion to generate the Fibonacci sequence in Python. -->

### Exercise 5: Print Comb

Write a Python program that prints all possible combinations of two digits between 012 and 789. The digits of left should always be less than the digits on the right.
This reminds you something ?


<!-- exercice with decorators -->
### Exercise 6: Decorators

This is a function `say_hello`.
```python
@repeat(3)
def say_hello():
    print("Hello!")
```

Create a Python decorator that repeats the function call n times. In this example, the function should be called three times.

# [Next course : Control Flow](control-flow.md)