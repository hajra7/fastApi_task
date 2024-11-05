# models.py

from typing import List

class Task:
    def __init__(self, id: int, title: str, completed: bool = False):
        self.id = id
        self.title = title
        self.completed = completed

# In-memory list to store tasks
tasks: List[Task] = []
task_id_counter = 1  # Counter to assign unique IDs to tasks
