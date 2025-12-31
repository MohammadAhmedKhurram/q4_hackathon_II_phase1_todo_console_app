# Trace: T018
import pytest
from src.models.task import Task, ValidationError


def test_task_title_validation():
    with pytest.raises(ValidationError):
        Task(id=1, title="   ")

    t = Task(id=1, title="Buy milk")
    assert t.title == "Buy milk"
