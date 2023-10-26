"""Generic SQLAlchemy repository"""

# Local
from src.modules.shared.domain import AbstractRepository, Entity
from src.modules.shared.infrastructure import Base, SQLAlchemyDataMapper

# Third-parties
from sqlalchemy.orm import Session

# Build-ins
from typing import Type, Callable, List, Union

REMOVED = object()


class SQLAlchemyRepository(AbstractRepository):
    data_mapper: Type[SQLAlchemyDataMapper]

    def __init__(self, session: Session, identity_map=None) -> None:
        self.session = session
        self._identity_map = identity_map or dict()

    def __check_not_multiple_models(self):
        if self.data_mapper.multiple_models:
            raise NotImplementedError(
                'This repository does not support multiple models'
            )

    def add(self, entity: Type[Entity]):
        self.__check_not_multiple_models()
        self._identity_map[entity.id] = entity
        [instance] = self.data_mapper.entity_to_models(entity)
        self.session.add(instance)

    def remove(self, entity: Type[Entity]):
        self._check_not_removed(entity)
        self._identity_map[entity.id] = REMOVED
        self.__check_not_multiple_models()

        [model] = self.data_mapper.models
        instance = self.session.query(model).get(entity.id)
        self.session.delete(instance)

    def get_by_id(self, entity_id) -> Union[Type[Entity], None]:
        self.__check_not_multiple_models()
        [model] = self.data_mapper.models
        instance = self.session.get(model, entity_id)
        return self._get_entity(instance, self.data_mapper.models_to_entity)

    def all(self) -> Union[List[Type[Entity]], None]:
        self.__check_not_multiple_models()
        [model] = self.data_mapper.models
        instances = self.session.query(model).all()
        return [self._get_entity(instance, self.data_mapper.models_to_entity) for instance in instances]

    def last_id(self) -> int:
        self.__check_not_multiple_models()
        [model] = self.data_mapper.models
        instance = self.session.query(model).order_by(model.id.desc()).first()
        return instance.id if instance else 0

    def _get_entity(self, instances: List[Type[Base]], mapper_func: Callable):
        if not instances:
            return None

        if not isinstance(instances, list):
            instances = [instances]

        entity = mapper_func(instances)
        self._check_not_removed(entity)

        if entity.id in self._identity_map:
            return self._identity_map[entity.id]

        self._identity_map[entity.id] = entity
        return entity

    def _check_not_removed(self, entity: Type[Entity]):
        assert self._identity_map.get(
            entity.id, None
        ) is not REMOVED, f'Entity {entity.id} already removed'
