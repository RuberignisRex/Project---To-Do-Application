# Project: To Do List Application
# program must allow users to add, view, and delete tasks from a to-do list.

# Initial empty array that will be used to store tasks
tasks = []

# Defining main menu function.
# This function will display the main menu and handle user input.
def main_menu():
    while True:
        print("\nTo Do List Application")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            delete_task()
        elif choice == '4':
            print("Exiting.")
            break
        else:
            print("Error: Invalid choice. Please try again.")
            
# Function to add a task to the list
# This function prompts the user to enter a task and adds it to the tasks array.
def add_task():
    task = input("Enter a new task: ")
    if task:
        tasks.append(task)
        print(f'Your new task "{task}" has been added to the to do list.')
    else:
        print("Error: Task cannot be empty.")
    
# Function to view all tasks in the list
# This function displays all the tasks currently stored in the tasks array.
def view_tasks():
    if not tasks:
        print("Error: No current tasks to display.")
    else:
        print("Your To Do List:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
            
# Function to delete a task from the list
# This function prompts the user to enter a task number. It then deletes it from the tasks array.
def delete_task():
    if not tasks:
        print("Error: No current tasks to delete.")
        return

    view_tasks()
    try:
        task_num = int(input("Enter the task number to delete: "))
        if 1 <= task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)
            print(f'The task "{removed_task}" has been deleted from the to do list.')
        else:
            print("Error: Invalid task number.")
    except ValueError:
        print("Error: Please enter a number.")
        
# Starting the application by calling the main menu function
# This block ensures that the main menu is called when the script is run directly.
if __name__ == "__main__":
    try:
        main_menu()
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("Thank you for using the To Do List Application.")
