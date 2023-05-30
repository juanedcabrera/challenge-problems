# Directions:

# Given a string, return the character that is most
# commonly used in the string.

# Examples:

# ```
# maxChar("abcccccccd") === "c"
# maxChar("apple 1231111") === "1"
# ```

# def maxChar(string):
#     char_count = {}
#     for char in string:
#         if char in char_count:
#             char_count[char] += 1
#         else:
#             char_count[char] = 1
#     max_count = 0
#     max_char = ''
#     for char, count in char_count.items():
#         if count > max_count:
#             max_count = count
#             max_char = char
#     return max_char

# apple = maxChar("abcccccccd")
# print(apple)

def maxChar(string):
    charA = {}
    for char in string:
        if char in charA:
            charA[char] += 1
        else:
            charA[char] = 1
    max_count = 0
    max_char = ''
    for char, count in charA.items():
        if count > max_count:
            max_count = count
            max_char = char
    return max_char

apple = maxChar("abcccccccd")
print(apple)


