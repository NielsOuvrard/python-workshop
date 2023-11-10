def generate_fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        next_num = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_num)
    return fib_sequence

# Example usage:
terms = 10
fibonacci_sequence = generate_fibonacci(terms)
print("Fibonacci sequence with", terms, "terms:", fibonacci_sequence)
