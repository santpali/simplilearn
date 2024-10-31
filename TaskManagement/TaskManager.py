class TaskManager(object):

    tasks = []
    username = None
    #def __init__(self):
        # self.username = username;

    # Function to add a task
    def add_task(self, username, task_description):
        task_id = len(self.tasks) + 1  # Simple unique ID generation
        self.tasks.append({"id": task_id, "description": task_description, "status": "Pending"})
        print(f"Task added with ID: {task_id}")

    # Function to view tasks
    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
            return

        for task in self.tasks:
            print(f"ID: {task['id']}, Description: {task['description']}, Status: {task['status']}")

    # Function to mark a task as completed
    def mark_completed(self, task_id):
        for task in self.tasks:
            if task['id'] == task_id:
                task['status'] = 'Completed'
                print(f"Task ID {task_id} marked as completed.")
                return
        print("Task not found.")

    # Function to delete a task
    def delete_task(self, task_id):
        for task in self.tasks:
            if task['id'] == task_id:
                self.tasks.remove(task)
                print(f"Task ID {task_id} deleted.")
                return
        print("Task not found.")

    # Function to track budget
    def track_budget(self, budget):
        expenses = 0
        while True:
            expense = float(input("Enter an expense (or type 0 to finish): "))
            if expense == 0:
                break
            expenses += expense
            if expenses > budget:
                print("You have exceeded your budget!")
            else:
                remaining = budget - expenses
                print(f"You have ${remaining} left for the month.")
