# Write a program that prints the day of the week given a number of days and weeks.

# Example: 30 days from Monday is Wednesday.

# Answer the following questions:

# * Today is Sunday - What day of the week will it be in 100 days?
# * Today is Tuesday - What day of the week will it be in 4 weeks and 2 days?
# * Today is Friday - What day of the week will it be in 294 days?
# * Bonus: What month and day is it 73 days after October 31st 2018?


# NEED TO PRACTICE - I did not get how to solve - combined forces with Myles and got it


def day_of_the_week(today,num):
    weekdays = ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]
    index = int(weekdays.index(today))
    print(index)
    days = num % 7
    print(days)
    print(days + index)
    index2 = (index + days) % 7 # the remainder function is giving everything that's left over that hasn't been divided evenly
    print(index2)
    return weekdays[index2]

print(day_of_the_week("saturday", 16))

# take the indice and add the total numbe of days to it and then divide by 7 and then take the remainder and that will be the new indice