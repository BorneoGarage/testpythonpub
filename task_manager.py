import os
import json

TASKS_FILE = "tasks.json"

def load_tasks():
    """Load tasks from a file."""
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    """Save tasks to a file."""
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

def display_tasks(tasks):
    """Display all tasks."""
    if not tasks:
        print("\nNo tasks available.")
    else:
        print("\nTASK LIST:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task['title']} - {'Completed' if task['completed'] else 'Pending'}")

def add_task(tasks):
    """Add a new task."""
    title = input("\nEnter task title: ")
    tasks.append({"title": title, "completed": False})
    save_tasks(tasks)
    print("Task added successfully!")

def update_task(tasks):
    """Mark a task as completed."""
    display_tasks(tasks)
    try:
        index = int(input("\nEnter task number to mark as completed: ")) - 1
        if 0 <= index < len(tasks):
            tasks[index]["completed"] = True
            save_tasks(tasks)
            print("Task marked as completed!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task(tasks):
    """Delete a task."""
    display_tasks(tasks)
    try:
        index = int(input("\nEnter task number to delete: ")) - 1
        if 0 <= index < len(tasks):
            removed_task = tasks.pop(index)
            save_tasks(tasks)
            print(f"Task '{removed_task['title']}' deleted successfully!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    """Main function to run the Task Manager."""
    tasks = load_tasks()

    while True:
        print("\nTask Manager")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            display_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            update_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Exiting Task Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
