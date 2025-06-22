class ToDoList:
    def __init__(self):
        self.tasks = []
    
    def add_task(self, task):
        """Add a new task to the list"""
        self.tasks.append({"description": task, "completed": False})
        print(f"Task '{task}' added successfully!")
    
    def view_tasks(self):
        """Display all tasks with their status"""
        if not self.tasks:
            print("Your to-do list is empty!")
            return
        
        print("\nYour To-Do List:")
        for idx, task in enumerate(self.tasks, 1):
            status = "✓" if task["completed"] else " "
            print(f"{idx}. [{status}] {task['description']}")
    
    def complete_task(self, task_num):
        """Mark a task as completed"""
        try:
            if 1 <= task_num <= len(self.tasks):
                self.tasks[task_num-1]["completed"] = True
                print(f"Task {task_num} marked as completed!")
            else:
                print("Invalid task number!")
        except ValueError:
            print("Please enter a valid number!")
    
    def remove_task(self, task_num):
        """Remove a task from the list"""
        try:
            if 1 <= task_num <= len(self.tasks):
                removed = self.tasks.pop(task_num-1)
                print(f"Task '{removed['description']}' removed!")
            else:
                print("Invalid task number!")
        except ValueError:
            print("Please enter a valid number!")

def main():
    todo = ToDoList()
    
    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Remove Task")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == "1":
            task = input("Enter the task: ")
            todo.add_task(task)
        elif choice == "2":
            todo.view_tasks()
        elif choice == "3":
            todo.view_tasks()
            if todo.tasks:
                task_num = int(input("Enter task number to mark as completed: "))
                todo.complete_task(task_num)
        elif choice == "4":
            todo.view_tasks()
            if todo.tasks:
                task_num = int(input("Enter task number to remove: "))
                todo.remove_task(task_num)
        elif choice == "5":
            print("Exit")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
