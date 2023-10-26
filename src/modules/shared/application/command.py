"""Shared command stuffs"""

# Build-ins
from abc import ABC
from typing import Dict, Any, Type
from dataclasses import dataclass, field


class Command(ABC):
    """Abstract base class for the commands"""


@dataclass
class CommandResponse:
    entity_id: Any = None
    dto: Type[Command] = None
    extra_data: Dict[str, Any] = field(default_factory=dict)
    errors: Dict[str, Any] = field(default_factory=dict)

    @property
    def has_errors(self) -> bool:
        return len(self.errors) > 0
