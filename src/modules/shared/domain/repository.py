"""Abstract Repository"""

# Build-ins
from abc import ABC, abstractmethod
from typing import List, Type, Union

# Local
from src.modules.shared.domain import Entity


class AbstractRepository(ABC):
    entity: Type[Entity]

    @abstractmethod
    def add(self, entity: Type[Entity]):
        raise NotImplementedError

    @abstractmethod
    def remove(self, entity: Type[Entity]):
        raise NotImplementedError

    @abstractmethod
    def get_by_id(self, entity_id) -> Union[Type[Entity], None]:
        raise NotImplementedError

    @abstractmethod
    def all(self) -> Union[List[Type[Entity]], None]:
        raise NotImplementedError
