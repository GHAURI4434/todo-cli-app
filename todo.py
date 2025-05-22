def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            return [line.strip() for line in file]
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")

def show_tasks(tasks):
    print("\n📝 Your Tasks:")
    if not tasks:
        print("📭 No tasks found.")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")

def main():
    tasks = load_tasks()

    while True:
        print("\n=== To-Do List Menu ===")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Delete Task")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == '1':
            show_tasks(tasks)

        elif choice == '2':
            task = input("Enter new task: ").strip()
            if task:
                tasks.append(task)
                save_tasks(tasks)
                print("✅ Task added.")
            else:
                print("❌ Task cannot be empty.")

        elif choice == '3':
            show_tasks(tasks)
            try:
                num = int(input("Enter task number to delete: "))
                if 1 <= num <= len(tasks):
                    removed = tasks.pop(num - 1)
                    save_tasks(tasks)
                    print(f"🗑️ Removed: {removed}")
                else:
                    print("❌ Invalid task number.")
            except ValueError:
                print("❌ Please enter a valid number.")

        elif choice == '4':
            print("👋 Exiting To-Do List. Goodbye!")
            break

        else:
            print("❌ Invalid choice. Please enter 1-4.")

if __name__ == "__main__":
    main()
