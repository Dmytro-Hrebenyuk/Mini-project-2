def high_and_low(numbers):
    # Split the string of space-separated numbers into a list of integers
    num_list = [int(num) for num in numbers.split()]
    
    # Find the maximum and minimum numbers in the list
    max_num = max(num_list)
    min_num = min(num_list)
    
    # Return the highest and lowest numbers as a formatted string
    return f"{max_num} {min_num}"

# Test cases
print(high_and_low("1 2 3 4 5"))  # Output: "5 1"
print(high_and_low("1 2 -3 4 5")) # Output: "5 -3"
print(high_and_low("1 9 3 4 -5")) # Output: "9 -5"