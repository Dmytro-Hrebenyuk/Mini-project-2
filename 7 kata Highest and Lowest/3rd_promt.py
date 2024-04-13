def high_and_low(numbers):
    # Step 1: Split the string into individual numbers
    number_list = numbers.split()

    # Step 2: Convert each number from string format to integer format
    number_list = [int(num) for num in number_list]

    # Step 3: Find the highest and lowest numbers
    highest = max(number_list)
    lowest = min(number_list)

    # Step 4: Format the result as a string
    result = f"{highest} {lowest}"
    
    return result

# Test cases
print(high_and_low("1 2 3 4 5"))    # Output: "5 1"
print(high_and_low("1 2 -3 4 5"))   # Output: "5 -3"
print(high_and_low("1 9 3 4 -5"))   # Output: "9 -5"