# Define an empty list to store tasks
tasks = []


# Define a function to display the current tasks
def show_tasks():
    if tasks:
        print("Current tasks:")
        for i, task in enumerate(tasks):
            print(f"{i + 1}. {task}")
    else:
        print("No tasks.")


# Define a function to add a task
def add_task():
    task = input("Enter task: ")
    tasks.append(task)
    print(f"{task} added to tasks.")


# Define a function to delete a task
def delete_task():
    show_tasks()
    if tasks:
        task_index = int(input("Enter task number to delete: ")) - 1
        if 0 <= task_index < len(tasks):
            task = tasks.pop(task_index)
            print(f"{task} deleted from tasks.")
        else:
            print("Invalid task number.")
    else:
        print("No tasks to delete.")


# Define a function to update a task
def update_task():
    show_tasks()
    if tasks:
        task_index = int(input("Enter task number to update: ")) - 1
        if 0 <= task_index < len(tasks):
            new_task = input("Enter new task: ")
            tasks[task_index] = new_task
            print(f"{new_task} updated in tasks.")
        else:
            print("Invalid task number.")
    else:
        print("No tasks to update.")


# Define a function to quit the program
def quit_program():
    print("Goodbye!")
    quit()


# Define a dictionary to map user inputs to functions
options = {
    "1": show_tasks,
    "2": add_task,
    "3": delete_task,
    "4": update_task,
    "5": quit_program
}


# Define a function to display the menu and get user input
def menu():
    print("""
    To-Do List Manager

    1. Show Tasks
    2. Add Task
    3. Delete Task
    4. Update Task
    5. Quit
    """)
    choice = input("Enter an option: ")
    if choice in options:
        options[choice]()
    else:
        print("Invalid option.")


# Start the program
while True:
    menu()
