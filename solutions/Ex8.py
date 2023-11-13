temperatures = (30, 32, 28, 22, 30, 29, 24)

# 1. Find the average temperature for the week.
average_temperature = sum(temperatures) / len(temperatures)

# 2. Find the maximum temperature for the week.
max_temperature = max(temperatures)

# 3. Which day had the minimum temperature for the week?
min_temperature_day = None
min_temperature = min(temperatures)
for day, temperature in enumerate(temperatures, start=1):
    if temperature == min_temperature:
        min_temperature_day = day
        break

# 4. Check if the temperatures list contains a temperature of 27.
is_27_present = 27 in temperatures

# 5. What was the temperature on Thursday?
thursday_temperature = temperatures[1]  # Index 1 corresponds to Thursday

# 6. Create a new tuple with temperatures in Fahrenheit.
temperatures_fahrenheit = tuple((temp * 9/5) + 32 for temp in temperatures)

# After your code, print the results
print("Average Temperature:", average_temperature)
print("Maximum Temperature:", max_temperature)
print("Minimum Temperature is on Day", min_temperature_day)
print("Is 27 present?", is_27_present)
print("Temperature on Thursday:", thursday_temperature)
print("Temperatures in Fahrenheit:", temperatures_fahrenheit)
