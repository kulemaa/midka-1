def process_items():
    unique_items = set()
    non_unique_items = {}

    while True:
        user_input = input("Please chose the task you want to perform:\n\n1. Enter items\n\n2. Exit\n\nUser Input: ")

        if user_input == '1':
            items = input("Please enter items separated by comma\n\nUser Input: ").split(',')
            items = [item.strip() for item in items]

            for item in items:
                if item in unique_items:
                    if item in non_unique_items:
                        non_unique_items[item] += 1
                    else:
                        non_unique_items[item] = 2
                else:
                    unique_items.add(item)

            print("Items are saved")
            print("Unique items: " + str(unique_items))
            print("Not unique items: " + str([(item, count) for item, count in non_unique_items.items()]))

        elif user_input == '2':
            print("Exiting the program")
            break

        else:
            print("Invalid input, please try again")

process_items()