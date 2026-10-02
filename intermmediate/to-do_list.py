import json
import os

print("JSON file location:", os.path.abspath("tasks.json"))

FILE_NAME = os.path.join(os.path.dirname(os.path.abspath(__file__)), "tasks.json")


def load_tasks():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)


def add_task(tasks):
    task_name = input("Enter task: ")

    task = {
        "task": task_name,
        "completed": False
    }

    tasks.append(task)
    save_tasks(tasks)

    print("Task added successfully!")


def view_tasks(tasks):
    if len(tasks) == 0:
        print("No tasks found.")
        return

    print("\n===== YOUR TASKS =====")

    for i in range(len(tasks)):
        if tasks[i]["completed"]:
            status = "Done"
        else:
            status = "Pending"

        print(i + 1, ".", tasks[i]["task"], "-", status)


def delete_task(tasks):
    view_tasks(tasks)

    if len(tasks) == 0:
        return

    try:
        task_number = int(input("Enter task number to delete: "))

        if task_number < 1 or task_number > len(tasks):
            print("Error: Task does not exist.")
            return

        tasks.pop(task_number - 1)
        save_tasks(tasks)

        print("Task deleted successfully!")

    except ValueError:
        print("Error: Please enter a valid number.")


def mark_done(tasks):
    view_tasks(tasks)

    if len(tasks) == 0:
        return

    try:
        task_number = int(input("Enter task number to mark as done: "))

        if task_number < 1 or task_number > len(tasks):
            print("Error: Task does not exist.")
            return

        tasks[task_number - 1]["completed"] = True
        save_tasks(tasks)

        print("Task marked as completed!")

    except ValueError:
        print("Error: Please enter a valid number.")


tasks = load_tasks()

while True:
    print("\n===== TO-DO LIST =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Mark Task as Done")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_task(tasks)

    elif choice == "2":
        view_tasks(tasks)

    elif choice == "3":
        delete_task(tasks)

    elif choice == "4":
        mark_done(tasks)

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Error: Invalid choice.")