"""Shared Configuration File"""

# Build-ins
import os


class Config:
    DATABASE_DRIVER = 'postgresql+psycopg2'
    DATABASE_HOST = os.environ.get('DB_HOST', 'localhost')
    DATABASE_PORT = os.environ.get('DB_PORT', 5432)
    DATABASE_USER = os.environ.get('DB_USER', 'root')
    DATABASE_PASSWORD = os.environ.get('DB_PASSWORD')
    DATABASE_NAME = os.environ.get('DB_NAME')

    DEBUG = os.environ.get('DEBUG', False)
    DEFAULT_DATE_FORMAT = '%Y-%m-%d'
