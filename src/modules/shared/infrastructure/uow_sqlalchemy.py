"""SQLAlchemy Unit Of Work"""

# Shared
from src.modules.shared.application import AbstractUnitOfWork
from src.modules.shared.infrastructure import Config

# SQLAlchemy Repositories
# Import here the SQLAlchemy repositories

# Third-parties
from sqlalchemy import create_engine, engine
from sqlalchemy.orm import sessionmaker


DEFAULT_SESSION_FACTORY = sessionmaker(
    create_engine(
        engine.URL.create(
            drivername=Config.DATABASE_DRIVER,
            username=Config.DATABASE_USER,
            password=Config.DATABASE_PASSWORD,
            host=Config.DATABASE_HOST,
            port=Config.DATABASE_PORT,
            database=Config.DATABASE_NAME,
        )
    )
)


class SQLAlchemyUnitOfWork(AbstractUnitOfWork):
    def __init__(self, session_factory=DEFAULT_SESSION_FACTORY):
        self.session_factory = session_factory

    def __enter__(self):
        self.session = self.session_factory()
        # Set here the repositories
        # self.dummy_repository = SQLAlchemyDummyRepository(
        #     self.session
        # )
        return super().__enter__()

    def __exit__(self, *args):
        super().__exit__(*args)
        self.session.close()

    def commit(self):
        self.session.commit()

    def rollback(self):
        self.session.rollback()
