def display_menu():
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Done")
    print("4. Exit")

def add_task(tasks, task):
    tasks.append({"task": task, "done": False})
    print("Task added successfully!")

def view_tasks(tasks):
    if not tasks:
        print("No tasks to display.")
    else:
        print("Tasks:")
        for index, task in enumerate(tasks, start=1):
            status = "Done" if task["done"] else "Not Done"
            print(f"{index}. {task['task']} - {status}")

def mark_as_done(tasks, index):
    if 1 <= index <= len(tasks):
        tasks[index - 1]["done"] = True
        print("Task marked as done!")
    else:
        print("Invalid task index.")

def main():
    tasks = []

    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            task = input("Enter the task: ")
            add_task(tasks, task)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            index = int(input("Enter the index of the task to mark as done: "))
            mark_as_done(tasks, index)
        elif choice == "4":
            print("Exiting the to-do list. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
