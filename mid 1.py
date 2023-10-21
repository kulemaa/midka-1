try:
    name = input("Enter your name: ")
    salary = int(input("Enter your desired salary level: "))

    result = salary * 0.2

    print(f"Adam, the tax level you will pay with the salary {salary} is {result}")
except ValueError:
    print(f"{name}, please enter your desired salary as a digit")