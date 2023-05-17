# Directions:

# Given a string, return the character that is most
# commonly used in the string.

# Examples:

# ```
# maxChar("abcccccccd") === "c"
# maxChar("apple 1231111") === "1"
# ```

def maxChar(string):
    char_count = []
    for char in string:
        if char in char_count:
            (char_count[char]) += 1
        else:
            (char_count[char]) = 1
    return char_count

apple = slice(maxChar("apple 1231111"))
print(apple)
