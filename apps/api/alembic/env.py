from dotenv import load_dotenv
import os
from logging.config import fileConfig

from sqlalchemy import engine_from_config, pool
from alembic import context

# load .env
load_dotenv()

# Alembic Config object
config = context.config
fileConfig(config.config_file_name)

# override DB URL from .env
config.set_main_option(
    "sqlalchemy.url",
    f"postgresql+psycopg2://{os.getenv('POSTGRES_USER')}:{os.getenv('POSTGRES_PASSWORD')}@{os.getenv('POSTGRES_HOST')}:{5432}/{os.getenv('POSTGRES_DB')}"
)

# 👇 import your models and set metadata
from apps.api.models import Base  # adjust import path to your structure

target_metadata = Base.metadata

def run_migrations_offline():
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
    )

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )
    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
        )
        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()