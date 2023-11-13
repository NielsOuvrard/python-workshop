# Chapter 6: Tuples in Python

Tuples are ordered, immutable collections in Python that are similar to lists but have some key differences. In this chapter, we will explore the characteristics of tuples and how they differ from other data structures.

### Creating Tuples

In Python, tuples are created by enclosing a comma-separated sequence of values within parentheses.

```python
my_tuple = (1, 2, 3, 4, 5)
```

### Accessing Elements

Accessing elements in a tuple is similar to accessing elements in a list. Tuples are zero-indexed, so the first element is at index 0.

```python
element = my_tuple[2]  # Access the third element (3)
```

### Immutability of Tuples

One distinctive feature of tuples is their immutability. Once a tuple is created, its elements cannot be changed or modified.

```python
# This will result in an error
my_tuple[0] = 10
```

### Use Cases for Tuples

Tuples are suitable for situations where the data should remain constant throughout the program's execution. Common use cases include:

- **Returning Multiple Values** Functions can return multiple values as a tuple.

```python
def get_coordinates():
    return (10, 20)
```

- **Dictionary Keys** Tuples can be used as keys in dictionaries.

```python
coordinates_dict = {(10, 20): 'Location A', (30, 40): 'Location B'}
```

- **Unpacking Tuples** Tuples can be unpacked into multiple variables.

```python
x, y = get_coordinates()
```

### Iterating Through Tuples

Similar to lists, you can iterate through the elements of a tuple using a `for` loop.

```python
for item in my_tuple:
    print(item)
```

### Comparing Tuples with Other Data Structures

Tuples share similarities with lists but differ in immutability. Key points include:

- **Immutability** Tuples are immutable, whereas lists are mutable.
- **Use Cases** Tuples are often used for fixed collections of data, while lists are more versatile for dynamic collections.

Example: Tuple Operations

```python
# Tuple manipulation
my_tuple = (1, 2, 3, 4, 5)
concatenated_tuple = my_tuple + (6, 7, 8)
sliced_tuple = my_tuple[1:4]

print(concatenated_tuple)  # Output: (1, 2, 3, 4, 5, 6, 7, 8)
print(sliced_tuple)        # Output: (2, 3, 4)
```

In summary, tuples in Python provide an immutable and ordered way to store and handle data, offering advantages in specific scenarios where immutability is desired.



## [Next chapter: Python vs. C](python-vs-c.md)

### [Back to last chapter: Dictionaries](dictionaries.md)

### Or, you can go directly to the exercices [here](../exercices/exercices.md)