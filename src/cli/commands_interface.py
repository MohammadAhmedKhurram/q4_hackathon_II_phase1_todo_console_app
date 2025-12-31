# Trace: helper interface for CLI usage examples
from src.cli.commands import CLI
from src.store.in_memory_task_store import InMemoryTaskStore
from src.services.task_service import TaskService


def make_cli():
    store = InMemoryTaskStore()
    service = TaskService(store)
    return CLI(service)
