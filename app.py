from tasks import TaskManager
from utils import get_description, print_tasks
from storage import save_tasks, load_tasks

def main():
    manager = TaskManager()
    load_tasks(manager)

    print("Welcome to the Task Tracker CLI app.")
    print("Type a command to begin")

    while True:
        input_cmd = input().strip()

        if input_cmd.startswith("task-cli add"):
            desc = get_description(input_cmd)
            if desc:
                task = manager.add_task(desc)
                save_tasks(manager)
                print(f"Task added successfully (ID: {task.id})")
            else:
                print("Please provide a task description.")

        elif input_cmd.startswith("task-cli update"):
            parts = input_cmd.replace("task-cli update", "").strip().split(" ", 1)
            if len(parts) < 2 or not parts[0].isdigit():
                print("Please provide a valid task ID and description.")
                continue
            task_id = int(parts[0])
            desc = get_description(parts[1])
            if manager.update_task(task_id, desc):
                save_tasks(manager)
                print("Task updated successfully.")
            else:
                print("Task not found.")

        elif input_cmd.startswith("task-cli delete"):
            tid = input_cmd.replace("task-cli delete", "").strip()
            if tid.isdigit() and manager.delete_task(int(tid)):
                save_tasks(manager)
                print("Task deleted successfully.")
            else:
                print("Please provide a valid task ID.")

        elif input_cmd.startswith("task-cli mark-in-progress"):
            tid = input_cmd.replace("task-cli mark-in-progress", "").strip()
            if tid.isdigit() and manager.mark_in_progress(int(tid)):
                save_tasks(manager)
                print("Task marked as in progress successfully.")
            else:
                print("Task not found.")

        elif input_cmd.startswith("task-cli mark-done"):
            tid = input_cmd.replace("task-cli mark-done", "").strip()
            if tid.isdigit() and manager.mark_done(int(tid)):
                save_tasks(manager)
                print("Task marked as done successfully.")
            else:
                print("Task not found.")

        elif input_cmd.startswith("task-cli list"):
            param = input_cmd.replace("task-cli list", "").strip()
            tasks = manager.list_tasks(param)
            if tasks:
                print_tasks(tasks, param)
            else:
                print("No tasks available.")

        elif input_cmd == "task-cli help":
            print("\nTask Manager Commands:")
            print("task-cli add <description>               - Add a task")
            print("task-cli update <task_id> <description>  - Update a task")
            print("task-cli delete <task_id>                - Delete a task")
            print("task-cli mark-in-progress <task_id>      - Mark a task as in progress")
            print("task-cli mark-done <task_id>             - Mark a task as done")
            print("task-cli list                            - List all tasks")
            print("task-cli list todo                       - List all Todo tasks")
            print("task-cli list done                       - List all completed tasks")
            print("task-cli list in-progress                - List all in-progress tasks")
            print("task-cli exit                            - Exit the application")

        elif input_cmd == "task-cli exit":
            print("Exiting...")
            break

        else:
            print("Invalid Input.\nType 'task-cli help' for available commands.")

        print("Type a command to begin")

if __name__ == "__main__":
    main()
