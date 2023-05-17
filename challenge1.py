
# Most effecient way to guess a random number in a range:

# You are given a range of values, and you must write an algorithm to guess a random number in the range in the most effecient way possible.

# After every time you guess, you're told if you're right, too high, or too low.

###########

# low and high
# target number in head
# user would validate correct, high, or low
# inclusive - so that means that high and low would also be possible

def gather_input():
    high = int(input("What number would you like to put as the high value?"))
    low = int(input("What number would you like to put as the low value?"))
    while low <= high:
        middle = (low + high) // 2
        answer = input(f"Is your number {middle}? Yes or No: ")
        if answer == "Yes":
            print("Yay, got your number")
            return middle 
        else:
            answer = input(f"Is my number to high? Yes or No: ")
            if answer == "Yes":
                high = middle - 1
            else:
                low = middle + 1
    print("It was fun playing this game with you")

gather_input()




    # # setup
    # def binary_search(low, high, target):
    # # determine the middle
    #     while low <= high:
    # # run through loop to half things
    #         middle = (low + high) // 2
    #         if middle == target:
    #             return middle
    #         elif middle < target:    
    #             low = middle + 1
    #             print(f"My guess is too low. I picked {middle}, Guess again.")
    #         else:
    #             high = middle - 1
    #             print(f"My guess is too high. I picked {middle}, Guess again.")
    #     else:
    #         print(f"You guessed incorrectly.")
    #         return -1
            


    # low = 0
    # high = 10
    # target = 
    # index = binary_search(low, high, target)
    # print(f"You guessed correctly! You picked {target}")