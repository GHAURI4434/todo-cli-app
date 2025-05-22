import json
import os
from datetime import datetime

TASKS_FILE = "tasks.json"

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

def show_tasks(tasks):
    if not tasks:
        print("\n📭 No tasks available.")
        return
    print("\n📝 To-Do List:")
    for i, task in enumerate(tasks, 1):
        status = "✔️" if task['completed'] else "❌"
        print(f"{i}. [{status}] {task['task']} (Due: {task['due_date']})")

def add_task(tasks):
    task_name = input("Enter task description: ").strip()
    if not task_name:
        print("❌ Task cannot be empty.")
        return

    due_date = input("Enter due date (YYYY-MM-DD): ").strip()
    try:
        datetime.strptime(due_date, "%Y-%m-%d")
    except ValueError:
        print("❌ Invalid date format. Use YYYY-MM-DD.")
        return

    task = {
        "task": task_name,
        "due_date": due_date,
        "completed": False
    }
    tasks.append(task)
    save_tasks(tasks)
    print("✅ Task added.")

def delete_task(tasks):
    show_tasks(tasks)
    try:
        index = int(input("Enter task number to delete: ")) - 1
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            save_tasks(tasks)
            print(f"🗑️ Removed: {removed['task']}")
        else:
            print("❌ Invalid task number.")
    except ValueError:
        print("❌ Please enter a number.")

def mark_complete(tasks):
    show_tasks(tasks)
    try:
        index = int(input("Enter task number to mark as complete/incomplete: ")) - 1
        if 0 <= index < len(tasks):
            tasks[index]["completed"] = not tasks[index]["completed"]
            save_tasks(tasks)
            status = "completed" if tasks[index]["completed"] else "incomplete"
            print(f"✅ Task marked as {status}.")
        else:
            print("❌ Invalid task number.")
    except ValueError:
        print("❌ Please enter a number.")

def main():
    tasks = load_tasks()
    while True:
        print("\n=== Advanced To-Do List ===")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Delete Task")
        print("4. Mark Task Complete/Incomplete")
        print("5. Exit")

        choice = input("Choose an option (1-5): ").strip()

        if choice == '1':
            show_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            delete_task(tasks)
        elif choice == '4':
            mark_complete(tasks)
        elif choice == '5':
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice.")

if __name__ == "__main__":
    main()
