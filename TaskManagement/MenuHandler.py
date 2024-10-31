from TaskManagement.Authenticator import Authenticator
from TaskManagement.Registration import Registration
from TaskManagement.TaskManager import TaskManager

regUser = Registration()
taskManager = TaskManager()
# Main interactive menu function
def main():
    global taskManager
    tasks = []
    username = None
    while True:
        if username is None:
            print("1. Register\n2. Login\n3. Exit")
            choice = input("Choose an option: ")
            if choice == "1":
                register()
            elif choice == "2":
                username = login()
            elif choice == "3":
                break
        else:
            print("\nMenu:\n1. Add Task\n2. View Tasks\n3. Mark Task as Completed\n4. Delete Task\n5. Track Budget\n6. Logout")
            choice = input("Choose an option: ")
            if choice == "1":
                add_task(username)
            elif choice == "2":
                taskManager.view_tasks()
            elif choice == "3":
                mark_completed()
            elif choice == "4":
                delete_task()
            elif choice == "5":
                track_budget()
            elif choice == "6":
                username = None  # Log out
            else:
                print("Invalid option. Please try again.")

def register():
    username = input("Enter a username: ")
    password = input("Enter a password: ")
    regUser.registerUser(username,password)

# Function to login a user
def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    auth =Authenticator()
    return auth.login(username, password)

def add_task(username):
        task_description = input("Enter task description: ")
        taskManager.add_task(username, task_description)

# Function to mark a task as completed
def mark_completed():
    task_id = int(input("Enter task ID to mark as completed: "))
    taskManager.mark_completed(task_id)


# Function to delete a task
def delete_task():
    task_id = int(input("Enter task ID to delete: "))
    taskManager.delete_task(task_id)

# Function to track budget
def track_budget():
    budget = float(input("Enter your monthly budget: "))
    taskManager.track_budget(budget)

if __name__ == "__main__":
    main()