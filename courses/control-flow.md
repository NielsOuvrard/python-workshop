# Chapter 3: Control Flow

Control flow is a fundamental aspect of programming that allows you to make decisions and control the execution of your code. In this chapter, we will explore the control flow structures in Python and compare them to what you are familiar with in C programming.

### Conditional Statements

In Python, conditional statements are used to make decisions based on the truth or falsehood of expressions. Python's conditional statements are often simpler and more intuitive than C's.

#### `if`, `elif`, and `else`

In Python, you use the `if`, `elif` (short for "else if"), and `else` statements to create conditional blocks. Here's a Python example:

```python
# Python's if, elif, and else
x = 10
if x > 10:
    print("x is greater than 10")
elif x == 10:
    print("x is equal to 10")
else:
    print("x is less than 10")
```

In C, you would use the familiar if, else if, and else:

```c
// C's if, else if, and else
int x = 10;
if (x > 10) {
    printf("x is greater than 10");
} else if (x == 10) {
    printf("x is equal to 10");
} else {
    printf("x is less than 10");
}
```
### Ternary Operator

Python also has a concise ternary operator for conditional expressions, which is similar to the conditional (ternary) operator in C.

```python
# Python's ternary operator
x = 5
result = "greater than 10" if x > 10 else "less than or equal to 10"
```
```c
// C's ternary operator
int x = 5;
char *result = x > 10 ? "greater than 10" : "less than or equal to 10";
```

## Loops
Python offers two main loop structures: for and while. These loops have similarities with C loops, but the syntax is more straightforward.

`for` Loop
In Python, the for loop is primarily used for iterating over sequences (like lists) or other iterable objects.

### Iterating Through Lists
```python
# Python's for loop
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
````

In C, you might use a for loop like this:
```c
// C's for loop
char *fruits[] = {"apple", "banana", "cherry"};
for (int i = 0; i < 3; i++) {
    printf("%s\n", fruits[i]);
}
```

### Iterating Through a Range

Python's for loop can also be used to iterate through a range of numbers.

```python
# Python's for loop with range
for i in range(5):
    print(i)
```

```c
// C's for loop with range
for (int i = 0; i < 5; i++) {
    printf("%d\n", i);
}
```

`while` Loop
The while loop in Python works similarly to the while loop in C, with a condition to control the loop.

```python
# Python's while loop
count = 0
while count < 5:
    print(count)
    count += 1
```
```c
// C's while loop
int count = 0;
while (count < 5) {
    printf("%d\n", count);
    count++;
}
```

## Iterating Through Sequences
Python's `for` loop can be used to iterate through sequences, but it's often more concise and readable than C's for loop when working with `lists`, `tuples`, and `other iterable objects`.

In this chapter, we've explored Python's control flow structures, including conditional statements and loops, and compared them to similar constructs in C. In the next chapter, we'll dive into functions, which play a crucial role in both languages.

# [Next Chapter: Functions](functions.md)
