def is_palindrome(string):
    return string == string[::-1]

# Example usage:
word = "racecar"
result = is_palindrome(word)
print("Is the word a palindrome?", result)
