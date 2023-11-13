
# Chapter 3: Functions

In this chapter, we will delve into the world of functions in Python and draw comparisons to your experience with functions in C programming.

## Defining Functions

Python functions are defined using the `def` keyword, which is different from the `int` or `void` type declarations in C.

### Function Declaration in C

In C, you might define a function as follows:

```c
void print_add(int a, int b)
{
    printf("%d", a + b);
}
```

## Function Definition in Python
In Python, it's more concise:

```python
def print_add(a, b):
    print(a + b)
```

## Calling Functions
Calling functions in Python is straightforward. You can call a function by using its name followed by parentheses.

### Function Call in C
In C, you would call a function like this:

```c
int result = mul(3, 5);
```
### Function Call in Python
In Python, it's similar:
```python
result = mul(3, 5)
```

## Return Values
Python functions, like C functions, can return values. However, Python doesn't require you to specify a return type.

Return in C
In C, you specify the return type in the function declaration:

```c
int mul(int a, int b)
{
    return a * b;
}
```
Return in Python
In Python, you don't specify the return type:

```python
def mul(a, b):
    return a * b
```

## Variable number of arguments
Python functions can accept a variable number of arguments.
In C, this exist with variadic functions.

```python
def add(*args):
    result = 0
    for arg in args:
        result += arg
    return result

add(1, 2, 3, 4, 5)  # 15
```

```c
int add(int count, ...)
{
    int result = 0;
    va_list args;
    va_start(args, count);
    for (int i = 0; i < count; i++) {
        result += va_arg(args, int);
    }
    va_end(args);
    return result;
}

add(5, 1, 2, 3, 4, 5);  // 15
```
---

## Exist only in Python:

1. ## Default Arguments
Python allows you to define functions with default argument values, which is not a feature in C. This makes Python functions more flexible.

```python
def greet(name="Guest"):
    print("Hello, " + name + "!")
```

2. ## Lambda Functions
Python supports lambda functions, which are small, anonymous functions defined using the lambda keyword. They are similar in concept to function pointers in C.
```python
square = lambda x: x ** 2
```

3. ## Function Overloading
Python does not support function overloading like C++. In Python, a function can only have one definition.

In this chapter, we've explored the basics of functions in Python, highlighting the differences and similarities with C. Functions play a critical role in both languages, and understanding how they work in Python will be valuable as we proceed in this workshop.

```python
def greet(first_name, last_name):
    print("Hello, " + first_name + " " + last_name + "!")

def greet(first_name):
    print("Hello, " + first_name + "!")

greet("John")  # "Hello, John!"
```

4. ## Multiple return values
Python functions can return multiple values, while C functions can only return one value.

```python
def get_name():
    return "John", "Doe"

first_name, last_name = get_name()
```

5. ## Keyword Arguments
Python functions can accept keyword arguments, which are arguments preceded by an identifier when calling a function. This is not a feature in C.

```python
def greet(first_name, last_name):
    print("Hello, " + first_name + " " + last_name + "!")

greet(last_name="Doe", first_name="John") # "Hello, John Doe!"
greet(first_name="John", last_name="Doe") # "Hello, John Doe!"
```

6. ## Nested Functions

Python allows you to define functions inside other functions, which is not a feature in C.
```python
def outer():
    def inner():
        print("Hello from inner function!")
    inner()
```

7. ## Decorators
Python supports decorators, which are functions that modify the behavior of other functions. This is not a feature in C.

```python
# Decorator
def uppercase(func):
    def wrapper():
        result = func()
        return result.upper()
    return wrapper

# Decorated function
@uppercase
def greet():
    return "Hello, world!"

greet()  # "HELLO, WORLD!"
```
> [!INFO]\
> The @uppercase syntax is a shorthand way of saying `greet = uppercase(greet)`

8. ## Generators
Python supports generators, which are functions that can be paused and resumed, allowing for lazy evaluation of values. This is not a feature in C.

```python
def countdown(n):
    while n > 0:
        yield n
        n -= 1

for i in countdown(5):
    print(i)  # 5, 4, 3, 2, 1
```

9.  ## Closures
Python supports closures, which are functions that can access variables defined in an enclosing scope. This is not a feature in C.

```python
def outer():
    x = 42
    def inner():
        print(x)
    return inner

inner = outer()
inner()  # 42
```

# [Next Chapter: Lists and Iteration](lists-and-iteration.md)

## [Back to last chapter: Control Flow](control-flow.md)