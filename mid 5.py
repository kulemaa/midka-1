import time

tasks = []
completed_tasks = []

while True:
    print("\nPlease chose the task you want to perform:")
    print("\n1. Add Task")
    print("2. View All Tasks")
    print("3. Mark Task as Completed")
    print("4. View All Completed Tasks")
    print("5. Exit")

    user_input = input("\nUser Input: ")

    if user_input == '1':
        task_name = input("\nEnter the task: ")
        tasks.append(task_name)
        print(f'\nThe task "{task_name}" was added to the todo list')

    elif user_input == '2':
        if len(tasks) == 0:
            print("\nNo tasks available")
        else:
            print("\nHere is your todo list:")
            for i, task in enumerate(tasks):
                print(f'{i + 1}. {task}')

    elif user_input == '3':
        task_name = input("\nEnter the name of the task: ")
        for task in tasks:
            if task == task_name:
                tasks.remove(task)
                completed_tasks.append(task)
                print(f'\nThe task {task_name} is marked as completed')
                break
        else:
            print(f'\nThe task {task_name} does not exist')

    elif user_input == '4':
        if len(completed_tasks) == 0:
            print("\nNo completed tasks available")
        else:
            print("\nHere is your list of completed tasks:")
            for i, task in enumerate(completed_tasks):
                print(f'{i + 1}. {task}')

    elif user_input == '5':
        print("\nExiting the program")
        break

    else:
        print("\nInvalid input, please try again")