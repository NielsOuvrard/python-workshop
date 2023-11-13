# Exercices

> ℹ️ solutions are available in the `solutions` directory.

## 1. Swap Two Variables

Write a Python program that swaps the values of two variables without using a temporary variable. For example, if `x` is 5 and `y` is 10, after swapping, `x` should be 10 and `y` should be 5.

<details>
    <summary> 🔍 Hint: Click to reveal</summary>
    ✨ You can use multiple return values to swap two variables in Python. ✨
    <a href="../courses/functions.md#Multiple-return-values">Python's multiple assignment</a>
</details>

[Solution](../solutions/Ex1.py)

## 2. Palindrome Checker

Create a Python function that checks whether a given string is a palindrome. A palindrome is a word, phrase, number, or other sequence that reads the same forward and backward (ignoring spaces, punctuation, and capitalization).

<details>
    <summary> 🔍 Hint: Click to reveal</summary>
    ✨ Do you know [::-1] and what it does ? ✨
    <a href="https://www.w3schools.com/python/python_howto_reverse_string.asp">Python's reverse string</a>
</details>

[Solution](../solutions/Ex2.py)

## 3. Fibonacci Sequence

Create a Python function that generates the Fibonacci sequence up to a specified number of terms. The Fibonacci sequence starts with 0 and 1, and each subsequent number is the sum of the two previous numbers.

It begins like this: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

<details>
    <summary> 🔍 Hint: Click to reveal</summary>
    ✨ You can use recursion to generate the Fibonacci sequence in Python. ✨
    <a href="https://www.programiz.com/python-programming/recursion">Python's recursion</a>
</details>

[Solution](../solutions/Ex3.py)

## 4. Print Comb

Write a Python program that prints all possible combinations of two digits between 012 and 789. The digits of left should always be less than the digits on the right.

This reminds you something ?
<!-- In Epitech pool, you had to do this exercice with a C program at the first day. -->

> No hint for this one, you can do it !

[Solution](../solutions/Ex4.py)

## 5. Repeat Function Call

This is a function `say_hello`.
```python
# use this function

@repeat(3)
def say_hello():
    print("Hello!")
```

Create a Python `repeat` that repeats the function call n times. In this example, the function should be called three times.

<details>
    <summary> 🔍 Hint: Click to reveal</summary>
    ✨ You can use a decorator to repeat a function call in Python. ✨
    <a href="../courses/functions.md#Decorators">Python's decorators</a>
</details>

[Solution](../solutions/Ex5.py)

## 6. Recreate the `range` function

Create a Python function that takes up to three arguments and returns a list of numbers in the specified range.
The function should work similarly to Python's built-in `range` function.

<details>
    <summary> 🔍 Hint: Click to reveal</summary>
    ✨ You can use Generator to create a range function in Python. ✨
    <a href="../courses/functions.md#Generators">Python's generators</a>
</details>

[Solution](../solutions/Ex6.py)

<!-- about dictionaries -->

## 7. Dictionary Manipulation

You are given a dictionary representing information about books in a library.

```python
library_books = {
    'book1': {'title': 'Python Basics', 'author': 'John Smith', 'genre': 'Programming'},
    'book2': {'title': 'Data Science Essentials', 'author': 'Alice Johnson', 'genre': 'Data Science'},
    'book3': {'title': 'History of Science', 'author': 'Michael Turner', 'genre': 'History'},
    'book4': {'title': 'Cooking Mastery', 'author': 'Emily White', 'genre': 'Cooking'},
    'book5': {'title': 'Artificial Intelligence', 'author': 'David Lee', 'genre': 'Programming'},
}
```

1. Add a new book to the library called `book6` with the title `Gardening for Beginners`, the author `Sarah Smith`, and the genre `Gardening`.
2. Remove `book3` from the library.
3. Change the genre of `book4` to `Cooking Basics`.
4. Print the titles of all the books in the library.
5. Print the author of `book1`.
6. Return a book containing the title `Data Science Essentials`.
7. Check if the library contains a book called `Cryptography`.
8. Creating a new dictionary `programming_books` containing all books with the genre `Programming`.

<details>
    <summary> 🔍 Hint: Click to reveal</summary>
    ✨ You can use the del keyword or the pop() method to remove a key-value pair from a dictionary. ✨
    <a href="../courses/dictionaries.md#Dictionary-operations">Python's dictionary operations</a>
</details>

[Solution](../solutions/Ex7.py)

## 8 Tuple Manipulation

You are given a tuple representing the temperatures in Celsius for a week.

```python
temperatures = (30, 32, 28, 22, 30, 29, 24)
```

1. Find the `average` temperature for the week.
2. Find the `maximum` temperature for the week.
3. Which day had the minimum temperature for the week?
4. Check if the temperatures list contains a temperature of `27`.
5. What was the temperature on Thursday?
6. Create a new tuple with temperatures in Fahrenheit.

```python
# Your code here

# After your code, print the results
print("Average Temperature:", average_temperature)
print("Maximum Temperature:", max_temperature)
print("Minimum Temperature is on", min_temperature_day)
print("Is 27 present?", is_27_present)
print("Temperature on Thursday:", thursday_temperature)
print("Temperatures in Fahrenheit:", temperatures_fahrenheit)
```

<details>
    <summary> 🔍 Hint: Click to reveal</summary>
    ✨ You can use the sum() and len() functions to calculate the average temperature ✨
    ✨ From Celsius to Fahrenheit : `F = (C * 9/5) + 32` ✨
    <a href="../courses/tuples.md#Iterating-Through-Tuples">Python's tuple operations</a>
</details>

[Solution](../solutions/Ex8.py)

> ## 🎉 Congratulations, you have finished the workshop !
