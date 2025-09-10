from models import Task
from datetime import datetime

class TaskManager:
    def __init__(self):
        self.tasks = {}
        self.task_id = 0

    def add_task(self, description: str) -> Task:
        self.task_id += 1
        task = Task(id=self.task_id, description=description)
        self.tasks[self.task_id] = task
        return task

    def update_task(self, task_id: int, description: str) -> bool:
        if task_id in self.tasks:
            task = self.tasks[task_id]
            task.description = description
            task.updatedAt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            return True
        return False
    
    def delete_task(self, task_id: int) -> bool:
        if task_id in self.tasks:
            del self.tasks[task_id]
            return True
        return False

    def mark_done(self, task_id: int) -> bool:
        if task_id in self.tasks:
            task = self.tasks[task_id]
            task.status = "done"
            task.updatedAt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            return True
        return False

    def mark_in_progress(self, task_id: int) -> bool:
        if task_id in self.tasks:
            task = self.tasks[task_id]
            task.status = "in-progress"
            task.updatedAt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            return True
        return False

    def list_tasks(self, status: str = "") -> list[Task]:
        if status:
            return [task for task in self.tasks.values() if task.status == status]
        return list(self.tasks.values())