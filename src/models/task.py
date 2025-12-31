# Trace: T002
from dataclasses import dataclass, field
from typing import Optional


class ValidationError(ValueError):
    pass


@dataclass
class Task:
    id: int
    title: str
    description: Optional[str] = None
    completed: bool = False

    def __post_init__(self):
        if not isinstance(self.title, str) or not self.title.strip():
            raise ValidationError("title must be a non-empty string")
