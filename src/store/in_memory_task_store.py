# Trace: T003
from typing import List, Optional
from threading import Lock

from src.models.task import Task, ValidationError


class TaskNotFoundError(KeyError):
    pass


class InMemoryTaskStore:
    def __init__(self):
        self._lock = Lock()
        self._next_id = 1
        self._tasks = {}

    def create(self, title: str, description: Optional[str] = None) -> Task:
        # validation is performed by Task
        task = Task(id=self._next_id, title=title, description=description, completed=False)
        with self._lock:
            self._tasks[self._next_id] = task
            self._next_id += 1
        return task

    def list_all(self) -> List[Task]:
        with self._lock:
            return list(self._tasks.values())

    def get_by_id(self, task_id: int) -> Task:
        with self._lock:
            try:
                return self._tasks[task_id]
            except KeyError:
                raise TaskNotFoundError(f"Task with id {task_id} not found")

    def update(self, task_id: int, title: Optional[str] = None, description: Optional[str] = None) -> Task:
        with self._lock:
            task = self._tasks.get(task_id)
            if not task:
                raise TaskNotFoundError(f"Task with id {task_id} not found")
            if title is not None:
                # re-use validation from Task by creating a new Task instance
                if not isinstance(title, str) or not title.strip():
                    raise ValidationError("title must be a non-empty string")
                task.title = title
            if description is not None:
                task.description = description
            self._tasks[task_id] = task
            return task

    def delete(self, task_id: int) -> None:
        with self._lock:
            if task_id in self._tasks:
                del self._tasks[task_id]
            else:
                raise TaskNotFoundError(f"Task with id {task_id} not found")

    def toggle(self, task_id: int) -> Task:
        with self._lock:
            task = self._tasks.get(task_id)
            if not task:
                raise TaskNotFoundError(f"Task with id {task_id} not found")
            task.completed = not task.completed
            self._tasks[task_id] = task
            return task
