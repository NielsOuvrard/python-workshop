def generate_fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return generate_fibonacci(n-1) + generate_fibonacci(n-2)

# Example usage:
for i in range(10):
    print(generate_fibonacci(i))
