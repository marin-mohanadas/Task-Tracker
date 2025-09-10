
# 📋 Task Tracker CLI

A simple command-line **Task Tracker** app built with Python.  
You can add, update, delete, and list tasks — all from your terminal. Tasks are saved to a JSON file so they persist between sessions.

This project is based on the [roadmap.sh Task Tracker project](https://roadmap.sh/projects/task-tracker).

---

## ✨ Features
- ➕ Add tasks with descriptions  
- 📝 Update tasks by ID  
- 🗑️ Delete tasks  
- ✅ Mark tasks as **done**  
- ⏳ Mark tasks as **in-progress**  
- 📂 List tasks by status (`todo`, `in-progress`, `done`)  
- 💾 Persistent storage using JSON  

---

## 🛠️ Project Structure
```
task_tracker/
│── app.py          # Entry point (CLI interface)
│── models.py       # Data model (Task class)
│── tasks.py        # Business logic (TaskManager)
│── storage.py      # JSON persistence (save/load tasks)
│── utils.py        # Helper functions (parsing, formatting)
│── tasks.json      # Auto-generated file to store tasks
│── test_tasks.py   # Unit tests for TaskManager
```

---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/task-tracker.git
cd task-tracker
```

### 2. Run the app
```bash
python app.py
```

---

## 💻 Usage

When you start the app, you’ll see:

```
Welcome to the Task Tracker CLI app.
Type a command to begin
```

### Commands

| Command | Description |
|---------|-------------|
| `task-cli add "description"` | Add a new task |
| `task-cli update <task_id> "new description"` | Update a task |
| `task-cli delete <task_id>` | Delete a task |
| `task-cli mark-in-progress <task_id>` | Mark task as in progress |
| `task-cli mark-done <task_id>` | Mark task as done |
| `task-cli list` | List all tasks |
| `task-cli list todo` | List only todo tasks |
| `task-cli list done` | List only completed tasks |
| `task-cli list in-progress` | List only in-progress tasks |
| `task-cli help` | Show all commands |
| `task-cli exit` | Exit the app |

---

## 📊 Example

```
task-cli add "Finish Python project"
task-cli add "Write README file"
task-cli list
```

Output:

```
Showing all tasks
ID    Description                                   Status          CreatedAt            UpdatedAt
----------------------------------------------------------------------------------------------------
1     Finish Python project                         todo            2025-09-08 12:30:10  2025-09-08 12:30:10
2     Write README file                             todo            2025-09-08 12:31:05  2025-09-08 12:31:05
----------------------------------------------------------------------------------------------------
```

---

## 🧪 Testing

Unit tests are included in **`test_tasks.py`**.  
They cover task creation, updating, deleting, status changes, and listing.

### Run tests with:
```bash
python -m unittest test_tasks.py
```

If you use **pytest**, you can also run:
```bash
pytest test_tasks.py
```

---

## 🛠️ Future Improvements
- Add deadlines and priorities for tasks  
- Export tasks to CSV or Markdown  
- Colored terminal output (using `rich` or `colorama`)  
- Unit tests for all functions  

---

## 📜 License
MIT License. Feel free to use and modify!  
