# Example 2: Decorator with arguments
def repeat(n):
    def decorator(func):
        def wrapper():
            for _ in range(n):
                func()
        return wrapper
    return decorator

@repeat(3)
def say_hello():
    print("Hello!")

# Using the decorated function
say_hello()