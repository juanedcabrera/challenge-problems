# Directions:
# Given an array and chunk size, divide the array into many subarrays
# where each subarray is of length size

# Examples:

# ```
# chunk([1, 2, 3, 4], 2) --> [[ 1, 2], [3, 4]]
# chunk([1, 2, 3, 4, 5], 2) --> [[ 1, 2], [3, 4], [5]]
# chunk([1, 2, 3, 4, 5, 6, 7, 8], 3) --> [[ 1, 2, 3], [4, 5, 6], [7, 8]]
# chunk([1, 2, 3, 4, 5], 4) --> [[ 1, 2, 3, 4], [5]]
# chunk([1, 2, 3, 4, 5], 10) --> [[ 1, 2, 3, 4, 5]]
# ```

# NEED TO PRACTICE - had to look up answer
def chunk(array, group):
    result = []
    index = 0
    while index < len(array):
        result.append(array[index:index + group]) # index:index+group is a slice method - kinda not a slice but using the start/stop/step
        index += group;
    return result

print(chunk([1, 2, 3, 4, 5], 2))
