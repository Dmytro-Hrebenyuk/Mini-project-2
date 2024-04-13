def high_and_low(numbers):
    # Split the string into a list of numbers
    numbers_list = list(map(int, numbers.split()))

    # Find the highest and lowest numbers
    highest = max(numbers_list)
    lowest = min(numbers_list)

    # Return the highest and lowest numbers as a string
    return f"{highest} {lowest}"

# Test cases
print(high_and_low("1 2 3 4 5"))   # return "5 1"
print(high_and_low("1 2 -3 4 5"))  # return "5 -3"
print(high_and_low("1 9 3 4 -5"))  # return "9 -5"