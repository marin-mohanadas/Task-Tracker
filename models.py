from dataclasses import dataclass
from datetime import datetime

@dataclass
class Task:
    id: int
    description: str
    status: str = "todo"
    createdAt: str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    updatedAt: str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
