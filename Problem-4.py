# Problem-4: Count multiples of 1-9 in a user-provided list
input_list = input("Enter numbers separated by commas: ")
numbers = [int(num.strip()) for num in input_list.split(",")]
divisors = [1,2,3,4,5,6,7,8,9]
count_dict = {}
for d in divisors:
    count = 0
    for num in numbers:
        if num % d == 0:
            count += 1
    count_dict[d] = count
print("\nOutput:")
print(count_dict)

