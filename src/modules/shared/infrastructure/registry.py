"""Registry Artifact"""

# Shared
from src.modules.shared.application import Command
from src.modules.shared.domain import Event

# Build-ins
from typing import Dict, Type, Callable, List


class Registry:
    """
    Registry class for registering command handlers and event handlers.
    """

    command_handlers: Dict[Type[Command], Callable] = {}
    event_handlers: Dict[Type[Event], List[Callable]] = {}

    def register_command_handler(self, command: Type[Command], handler: Callable):
        """
        Register a command handler.

        Args:
            command (Type[Command]): The command type.
            handler (Callable): The command handler function.

        Raises:
            AssertionError: If command is not a subclass of Command or handler is not callable.
        """
        assert issubclass(
            command, Command
        ), "command should be a subclass of Command"
        assert callable(handler), "handler should be a callable function"

        self.command_handlers[command] = handler

    def register_event_handler(self, event: Type[Event], handlers: List[Callable]):
        """
        Register an event handler.

        Args:
            event (Type[Event]): The event type.
            handlers (List[Callable]): The list of event handler functions.

        Raises:
            AssertionError: If event is not a subclass of Event or any of the handlers are not callable.
        """
        assert issubclass(event, Event), "event should be a subclass of Event"
        assert all(
            callable(handler)
            for handler in handlers
        ), "all handlers should be callable functions"

        self.event_handlers[event] = handlers
