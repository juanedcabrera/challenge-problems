#Write an algorithm to flatten a multi-dimensional array:

# ```
# vec = [[1,2,3], [4,5,6], [7,8,9]]
# => [1,2,3,4,5,6,7,8,9]
# ```

def flatten(vec):
    result = []
    for i in vec:
        result += i
    return result

vec = [[1,2,3], [4,5,6], [7,8,9]]
print(flatten(vec))

