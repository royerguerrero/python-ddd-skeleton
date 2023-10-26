"""Bootstrap Artifact"""

# Shared
from src.modules.shared.infrastructure import MessageBus, SQLAlchemyUnitOfWork, Registry
from src.modules.shared.application import AbstractUnitOfWork

from src.modules.shared.infrastructure import Config

# Build-ins
from typing import List
import logging


class Bootstrap:

    def __init__(
        self,
        registries: List[Registry],
        uow: AbstractUnitOfWork = SQLAlchemyUnitOfWork(),
        debug: bool = Config.DEBUG,
    ):
        self.uow = uow
        self._configure_logging(debug)

        self.bus = MessageBus(
            uow=self.uow,
            event_handlers=self._collect_event_handlers(registries),
            command_handlers=self._collect_command_handlers(registries),
        )

    def _configure_logging(self, debug: bool):
        if debug:
            logging.basicConfig(level=logging.DEBUG)
        else:
            logging.basicConfig(level=logging.INFO)

    def _collect_event_handlers(self, registries: List[Registry]):
        event_handlers = {}

        for registry in registries:
            event_handlers.update(registry.event_handlers)

        return event_handlers

    def _collect_command_handlers(self, registries: List[Registry]):
        command_handlers = {}

        for registry in registries:
            command_handlers.update(registry.command_handlers)

        return command_handlers

    def __call__(self):
        return self
