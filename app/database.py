"""Database settings."""

from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from .config import db_settings

async_engine = create_async_engine(
    url=db_settings.DATABASE_URL_asyncpg,
    echo=True,
    pool_size=5,
    max_overflow=10,
)
async_session = async_sessionmaker(bind=async_engine)


class Base(DeclarativeBase):
    """Base Model ORM class."""

    repr_cols_num = 3
    repr_cols = tuple()

    def __repr__(self) -> str:
        """Display the Model string representation.

        Don't use relationships here to avoid unexpected loads.
        """
        cols = []
        for idx, col in enumerate(self.__table__.columns.keys()):
            if col in self.repr_cols or idx < self.repr_cols_num:
                cols.append(f"{col}={getattr(self, col)}")

        return f"<{self.__class__.__name__}. {', '.join(cols)}>"
