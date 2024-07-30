# to_do_list.py

tasks = []

def display_tasks():
    print("To-Do List:")
    for i, task in enumerate(tasks, start=1):
        status = "Completed" if task["completed"] else "Not Completed"
        print(f"{i}. {task['task']} - {status}")

def add_task():
    task_name = input("Enter a new task: ")
    tasks.append({"task": task_name, "completed": False})
    print(f"Task '{task_name}' added!")

def complete_task():
    display_tasks()
    task_number = input("Enter the task number to mark as completed: ")
    try:
        task_number = int(task_number)
        if task_number > 0 and task_number <= len(tasks):
            tasks[task_number - 1]["completed"] = True
            print(f"Task {task_number} marked as completed!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid task number.")

def remove_task():
    display_tasks()
    task_number = input("Enter the task number to remove: ")
    try:
        task_number = int(task_number)
        if task_number > 0 and task_number <= len(tasks):
            del tasks[task_number - 1]
            print(f"Task {task_number} removed!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid task number.")

def main():
    while True:
        print("\nTo-Do List Application")
        print("1. Display To-Do List")
        print("2. Add a Task")
        print("3. Mark a Task as Completed")
        print("4. Remove a Task")
        print("5. Quit")
        choice = input("Enter your choice: ")
        if choice == "1":
            display_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            complete_task()
        elif choice == "4":
            remove_task()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()