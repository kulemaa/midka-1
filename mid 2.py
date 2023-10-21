try:
    print("Please chose the task you want to perform: ")
    operation = input("1. Addition \n2. Multiplication \n3. Division \n4. Exponentiation \n")
    num1 = float(input("Please enter the first numbers for addition, comma separated: "))
    num2 = float(input("Please enter the two numbers for addition, comma separated: "))

    if operation == '1':
        result = num1 + num2
    elif operation == '2':
        result = num1 * num2
    elif operation == '4':
        result = num1 ** num2
    elif operation == '3':
        if num2 == 0:
            print("Wrong")
        else:
            result = num1 / num2
    else:
        print("Wrong")

    if 'result' in locals():
        print(f"Result is: {result}")

except ValueError:
    print("Invalid input. Please enter valid numbers.")