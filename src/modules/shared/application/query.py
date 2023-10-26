"""Query Shared"""

# Build-ins
from dataclasses import dataclass, field
from typing import Type, Any, Dict


class Query:
    """Query Abstract"""

    def as_dict(self):
        """Return the data as a dict"""
        return self.__dict__


@dataclass
class QueryResponse:
    """Query Response"""

    dto: Type[Query] = None
    extra_data: Dict[str, Any] = field(default_factory=dict)
    errors: Dict[str, Any] = field(default_factory=dict)

    @property
    def has_errors(self) -> bool:
        return len(self.errors) > 0
