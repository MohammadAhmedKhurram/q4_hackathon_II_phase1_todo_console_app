# Trace: T008
from typing import Iterable
from src.models.task import Task


def format_task(task: Task) -> str:
    desc = f" - {task.description}" if task.description else ""
    status = "✓" if task.completed else " "
    return f"#{task.id} [{status}] {task.title}{desc}"


def render_task_list(tasks: Iterable[Task]) -> str:
    if not tasks:
        return "No tasks found."
    return "\n".join(format_task(t) for t in tasks)


def success_message_for_create(task: Task) -> str:
    return f"Created task #{task.id}: {task.title}"


def error_message(msg: str) -> str:
    return f"Error: {msg}"
