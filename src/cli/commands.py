# Trace: T006 T007 T009 T011 T012 T013
from typing import Optional

from src.services.task_service import TaskService
from src.store.in_memory_task_store import InMemoryTaskStore, TaskNotFoundError
from src.cli import ui
from src.models.task import ValidationError


class CLI:
    def __init__(self, service: TaskService):
        self.service = service

    def add(self, title: str, description: Optional[str] = None) -> str:
        try:
            task = self.service.add_task(title=title, description=description)
            return ui.success_message_for_create(task)
        except ValidationError as e:
            return ui.error_message(str(e))

    def list(self) -> str:
        tasks = self.service.list_tasks()
        return ui.render_task_list(tasks)

    def update(self, task_id: int, title: Optional[str] = None, description: Optional[str] = None) -> str:
        try:
            task = self.service.update_task(task_id=task_id, title=title, description=description)
            return f"Updated task #{task.id}"
        except TaskNotFoundError as e:
            return ui.error_message(str(e))
        except ValidationError as e:
            return ui.error_message(str(e))

    def toggle(self, task_id: int) -> str:
        try:
            task = self.service.toggle_task(task_id=task_id)
            return f"Toggled task #{task.id} -> {'completed' if task.completed else 'not completed'}"
        except TaskNotFoundError as e:
            return ui.error_message(str(e))

    def delete(self, task_id: int) -> str:
        try:
            self.service.delete_task(task_id=task_id)
            return f"Deleted task #{task_id}"
        except TaskNotFoundError as e:
            return ui.error_message(str(e))
