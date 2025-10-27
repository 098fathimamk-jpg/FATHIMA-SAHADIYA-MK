# Problem-2: Generate odd number series based on user input
while True:
    try:
        
        a = int(input("Enter the value of a: "))
        if a == 0:
            print("Program exited.")
            break
        print(f"Input a = {a}, then output :", end=" ")
        for i in range(1, a * 2, 2):
            if i < (a * 2 - 1):
                print(i, end=", ")
            else:
                print(i)

    except ValueError:
        print("Please enter a valid integer!")

