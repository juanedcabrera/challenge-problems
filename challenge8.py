# Direction:

# Given an amount of change, determine the minimum number of coins required to make that change

# Examples:

# ``` 
# greedy(65) --> 4 `(2 quarters, 1 dime,1 nickle)`
# greedy(5) --> 1 `(1 nickle)`
# ```

def greedy(num):
    coins = {'quarter': 25, 'dime': 10, 'nickel': 5, 'penny': 1}
    count = []

    for coin, value in coins.items():
        if num >= value:
            coin_count = num // value
            num -= coin_count * value
            count.append((coin, coin_count))

    return len(count)

print(greedy(65))