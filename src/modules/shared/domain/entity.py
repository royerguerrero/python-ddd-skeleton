"""Entity Abstract Class"""

# Build-ins
from abc import ABC
import uuid

# Domain
from src.modules.shared.domain import BusinessRule, BusinessRuleException


class Entity(ABC):
    """DO NOT USE THE __INIT__ METHOD to create the entity instead use a creator method"""
    id: uuid.UUID = lambda: globals()['Entity'].next_id()

    @classmethod
    def next_id(cls) -> uuid.uuid4:
        """Generate a new UUID"""
        return uuid.uuid4()

    def check_rule(self, rule: BusinessRule):
        """Checks if a rule is broken"""
        if rule.is_broken():
            raise BusinessRuleException(rule)

