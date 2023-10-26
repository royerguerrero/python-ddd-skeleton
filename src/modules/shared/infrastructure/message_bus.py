"""Message bus for manage the events"""

# Locals
from src.modules.shared.domain import Event, EventResponse, BusinessRuleException
from src.modules.shared.application import Command, CommandResponse, AbstractUnitOfWork

# Build-ins
from typing import List, Dict, Type, Callable, Union
from dataclasses import dataclass
import logging

Message = Union[Type[Command], Type[Event]]


@dataclass
class MessageBusResponse:
    command: List[CommandResponse]
    events: List[EventResponse]


class MessageBus:
    """MessageBus for Commands and Events"""

    def __init__(
        self,
        uow: AbstractUnitOfWork,
        event_handlers: Dict[Type[Event], List[Callable]],
        command_handlers: Dict[Type[Command], Callable]
    ):
        self.uow = uow
        self.event_handlers = event_handlers
        self.command_handlers = command_handlers

    def handle(self, message: Message) -> MessageBusResponse:
        self.queue = [message]
        command_response = None
        event_response = []

        while self.queue:
            message = self.queue.pop(0)
            if isinstance(message, Event):
                event_response = self.handle_event(message)
            elif isinstance(message, Command):
                command_response = self.handle_command(message)
            else:
                raise Exception(f'{message} was not Event or Command')

        return MessageBusResponse(command_response, event_response)

    def handle_event(self, message: Message):
        raise NotImplementedError

    def handle_command(self, message: Message) -> Union[CommandResponse, Exception]:
        logging.debug(f'🕹️ Handling command {message}')
        try:
            handler = self.command_handlers[type(message)]
            return handler(uow=self.uow, command=message)
        except BusinessRuleException as e:
            return CommandResponse(dto=message, errors={'BusinessRuleError': {'type': str(e)}})
        except Exception:
            logging.exception(f'🚨 Exception handing command {message}')
            raise
