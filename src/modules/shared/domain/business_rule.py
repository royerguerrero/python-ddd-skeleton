"""Business Rule"""

# Build-ins
from abc import ABC, abstractmethod


class BusinessRule(ABC):
    @abstractmethod
    def is_broken(self) -> bool:
        raise NotImplementedError
