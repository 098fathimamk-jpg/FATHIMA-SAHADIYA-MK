# Problem-4: Count multiples of 1-9 in a user-provided list

# Take input from user
input_list = input("Enter numbers separated by commas: ")

# Convert input string to a list of integers
numbers = [int(num.strip()) for num in input_list.split(",")]

# Divisors to check
divisors = [1,2,3,4,5,6,7,8,9]

# Dictionary to store counts
count_dict = {}

# Loop through each divisor
for d in divisors:
    count = 0
    for num in numbers:
        if num % d == 0:
            count += 1
    count_dict[d] = count

# Print the result
print("\nOutput:")
print(count_dict)
