"""In Memory Unit Of Work"""

# Shared
from src.modules.shared.application import AbstractUnitOfWork
from src.modules.shared.infrastructure import InMemoryRepository


class InMemoryUnitOfWork(AbstractUnitOfWork):
    # dummy_repository = InMemoryRepository()

    def __enter__(self):
        return super().__enter__()

    def __init__(self):
        self.committed = False

    def commit(self):
        self.committed = True

    def rollback(self):
        pass
