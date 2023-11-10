def my_range(start, stop=None, step=1):
    # If only one argument is provided, set start=0 and stop=argument
    if stop is None:
        stop = start
        start = 0

    while (step > 0 and start < stop) or (step < 0 and start > stop):
        yield start
        start += step

# Example usage:
for i in my_range(10, 0, -2):
    print(i)