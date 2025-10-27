# Problem-3: Generate series of numbers as per the given pattern
def odd_series(a):
    k = a if a % 2 == 1 else a - 1   
    result = []
    num = 1
    for _ in range(k):
        result.append(num)
        num += 2
    return result

count = 1  

while True:
    a = input("Enter the value of a: ")

    if a.lower() == 'x':
        print(f"{count}) input a = x, then output : 1, 3, 5, 7, 9, ...")
        break
    else:
        try:
            a = int(a)
            if a <= 0:
                print("Please enter a positive integer.")
                continue

            series = odd_series(a)
            print(f"{count}) input a = {a}, then output : " + ", ".join(str(n) for n in series))
            count += 1

        except ValueError:
            print("Invalid input! Enter an integer or 'x' to exit.")



