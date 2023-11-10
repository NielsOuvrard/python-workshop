def is_palindrome(string):
    # Remove spaces and convert to lowercase for case-insensitive comparison
    clean_string = string.replace(" ", "").lower()
    return clean_string == clean_string[::-1]

# Example usage:
word = "racecar"
result = is_palindrome(word)
print("Is the word a palindrome?", result)
