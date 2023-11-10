# Chapter 1: Variables and Data Types

In this chapter, we will explore the fundamental concepts of variables and data types in Python and compare them to what you are familiar with in C programming.

## Variables in Python

#### Variable Assignment

In Python, you can create variables without explicitly specifying their data types. This is quite different from C, where you must declare variables and specify their types. For example, in C, you might write:

```c
// C variable declaration
int number = 42;

char *name = "John";
```
In Python, it's much simpler:

```python
# Python variable assignment
number = 42

name = "John"
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

# [Next course : Control Flow](control-flow.md)

## [Back to main page](../readme.md)