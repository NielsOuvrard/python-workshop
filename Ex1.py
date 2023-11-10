def swap_variables(a, b):
    a, b = b, a
    return a, b

# Example usage:
a = 5
b = 10
a, b = swap_variables(a, b)
print("After swapping, a =", a, "and b =", b)
