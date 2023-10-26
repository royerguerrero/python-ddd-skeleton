"""Shared InMemory Repository"""

# Local
from src.modules.shared.domain import AbstractRepository, Entity

# Build-ins
from typing import List, Type, Union


class InMemoryRepository(AbstractRepository):
    """In memory repository"""

    def __init__(self) -> None:
        """Initialize the repository"""
        self.objects = {}

    def add(self, entity: Type[Entity]):
        """Add an entity to the repository"""
        self.objects[entity.id] = entity

    def remove(self, entity: Type[Entity]):
        """Remove an entity from the repository"""
        del self.objects[entity.id]

    def get_by_id(self, entity_id) -> Type[Entity]:
        """Get an entity by its id"""
        return self.objects.get(entity_id)

    def all(self) -> Union[List[Type[Entity]], None]:
        """Get all the entities"""
        return list(self.objects.values())
