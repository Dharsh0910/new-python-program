class Task:
    def __init__(self, task_id, title, description, status):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.status = status
    
    def __str__(self):
        return f"Task ID: {self.task_id}\nTitle: {self.title}\nDescription: {self.description}\nStatus: {self.status}"

class TaskManager:
    def __init__(self):
        self.tasks = []
        self.next_task_id = 1
    
    def create_task(self, title, description):
        task = Task(self.next_task_id, title, description, "Pending")
        self.tasks.append(task)
        self.next_task_id += 1
    
    def read_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        else:
            for task in self.tasks:
                print(task)
                print()
    
    def update_task(self, task_id, title=None, description=None, status=None):
        for task in self.tasks:
            if task.task_id == task_id:
                if title:
                    task.title = title
                if description:
                    task.description = description
                if status:
                    task.status = status
                return True
        return False
    
    def delete_task(self, task_id):
        for task in self.tasks:
            if task.task_id == task_id:
                self.tasks.remove(task)
                return True
        return False

# Test the application
def main():
    manager = TaskManager()
    
    # Create tasks
    manager.create_task("Task 1", "Complete feature A")
    manager.create_task("Task 2", "Test feature B")
    
    # Display tasks
    print("Tasks:")
    manager.read_tasks()
    
    # Update task
    print("Updating Task 1...")
    manager.update_task(1, title="Updated Task 1", description="Complete feature A and B", status="In Progress")
    
    # Display updated tasks
    print("\nUpdated Tasks:")
    manager.read_tasks()
    
    # Delete task
    print("Deleting Task 2...")
    manager.delete_task(2)
    
    # Display tasks after deletion
    print("\nTasks after deletion:")
    manager.read_tasks()

if __name__ == "__main__":
    main()
