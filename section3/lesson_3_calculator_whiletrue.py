while True:
    print("1-Addition\n2-Subtraction\n3-Multiplication\n4-Division\n0-Exit")
    operation = int(input("Select an operation: "))

    if operation == 0:
        break

    elif operation == 1:
        num1 = int(input("Enter the 1st number: "))
        num2 = int(input("Enter the 2nd number: "))
        print("Result:", num1 + num2)

    elif operation == 2:
        num1 = int(input("Enter the 1st number: "))
        num2 = int(input("Enter the 2nd number: "))
        print("Result:", num1 - num2)

    elif operation == 3:
        num1 = int(input("Enter the 1st number: "))
        num2 = int(input("Enter the 2nd number: "))
        print("Result:", num1 * num2)

    elif operation == 4:
        num1 = int(input("Enter the 1st number: "))
        num2 = int(input("Enter the 2nd number: "))
        if num2 != 0:
            print("Result:", num1 / num2)
        else:
            print("Error: Cannot divide by zero")
