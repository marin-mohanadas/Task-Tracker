import re
from models import Task

def get_description(input_str: str) -> str:
    matches = re.findall(r'"([^"]*)"', input_str)
    return matches[0] if matches else ""

def print_tasks(tasks: list[Task], status=""):
    print("Showing all tasks" if not status else f"Showing {status} tasks")
    print(f"{'ID':<5} {'Description':<50} {'Status':<15} {'CreatedAt':<20} {'UpdatedAt'}")
    print("-" * 100)
    for task in tasks:
        print(f"{task.id:<5} {task.description:<50} {task.status:<15} {task.createdAt:<20} {task.updatedAt}")
    print("-" * 100)
