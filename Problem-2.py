# Problem-2: Generate odd number series based on user input

# Loop to take multiple inputs (you can stop with any key)
while True:
    try:
        # Taking input from user
        a = int(input("Enter the value of a: "))

        # If user enters 0, stop the loop
        if a == 0:
            print("Program exited.")
            break

        # Generate and display odd number series up to 'a'
        print(f"Input a = {a}, then output :", end=" ")

        # Using for loop to generate odd numbers
        for i in range(1, a * 2, 2):
            # print each odd number with comma separation
            if i < (a * 2 - 1):
                print(i, end=", ")
            else:
                print(i)

    except ValueError:
        print("Please enter a valid integer!")
