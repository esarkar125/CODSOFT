# To-Do List Application

# Define an empty list to store tasks
tasks = []

# Function to add a task to the list
def add_task(task):
    tasks.append(task)
    print("Task added: " + task)

# Function to list all tasks
def list_tasks():
    if tasks:
        print("To-Do List:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    else:
        print("Your to-do list is empty.")

# Function to mark a task as complete
def complete_task(task_num):
    try:
        task_num = int(task_num)
        if 1 <= task_num <= len(tasks):
            completed_task = tasks.pop(task_num - 1)
            print(f"Task completed: {completed_task}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid task number.")

# Main loop
while True:
    print("\nOptions:")
    print("1. Add Task")
    print("2. List Tasks")
    print("3. Complete Task")
    print("4. Quit")
    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter the task: ")
        add_task(task)
    elif choice == "2":
        list_tasks()
    elif choice == "3":
        task_num = input("Enter the task number to mark as complete: ")
        complete_task(task_num)
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
