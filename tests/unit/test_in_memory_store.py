# Trace: T018
from src.store.in_memory_task_store import InMemoryTaskStore, TaskNotFoundError
from src.models.task import Task


def test_in_memory_store_create_and_list():
    store = InMemoryTaskStore()
    t1 = store.create("A", None)
    t2 = store.create("B", "desc")
    assert t1.id == 1
    assert t2.id == 2
    all_tasks = store.list_all()
    assert len(all_tasks) == 2


def test_get_update_delete_toggle():
    store = InMemoryTaskStore()
    t = store.create("Hello")
    fetched = store.get_by_id(1)
    assert fetched.title == "Hello"
    store.update(1, title="Hi")
    assert store.get_by_id(1).title == "Hi"
    store.toggle(1)
    assert store.get_by_id(1).completed is True
    store.delete(1)
    try:
        store.get_by_id(1)
        assert False, "Expected TaskNotFoundError"
    except TaskNotFoundError:
        pass
