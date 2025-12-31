# Trace: T004
from typing import List, Optional

from src.store.in_memory_task_store import InMemoryTaskStore, TaskNotFoundError
from src.models.task import Task, ValidationError


class TaskService:
    def __init__(self, store: InMemoryTaskStore):
        self.store = store

    def add_task(self, title: str, description: Optional[str] = None) -> Task:
        # domain validation handled by Task
        return self.store.create(title=title, description=description)

    def list_tasks(self) -> List[Task]:
        return self.store.list_all()

    def update_task(self, task_id: int, title: Optional[str] = None, description: Optional[str] = None) -> Task:
        return self.store.update(task_id=task_id, title=title, description=description)

    def delete_task(self, task_id: int) -> None:
        return self.store.delete(task_id)

    def toggle_task(self, task_id: int) -> Task:
        return self.store.toggle(task_id)
