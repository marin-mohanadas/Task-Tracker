import json
from tasks import TaskManager
from models import Task

def save_tasks(manager: TaskManager, filename="tasks.json"):
    data = {tid: vars(task) for tid, task in manager.tasks.items()}
    with open(filename, "w") as f:
        json.dump(data, f, indent=2)

def load_tasks(manager: TaskManager, filename="tasks.json"):
    try:
        with open(filename, "r") as f:
            data = json.load(f)
            for tid, t in data.items():
                task = Task(**t)
                manager.tasks[int(tid)] = task
                manager.task_id = max(manager.task_id, int(tid))
    except FileNotFoundError:
        pass
