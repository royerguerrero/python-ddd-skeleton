"""Abstract Value Object"""

# Build-ins
from abc import ABC


class ValueObject(ABC):
    """A value object abstract class
    Remember:
     - The value object is IMMUTABLE!
     - Validate in __init__ or __new__ methods
     - Use getters and setters
     - Overwrite __eq__ and __ne__ methods
    """
