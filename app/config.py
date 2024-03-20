"""Setting the database configuration for the app."""

from pydantic_settings import BaseSettings, SettingsConfigDict


class DBSettings(BaseSettings):
    """Main db configuration object."""

    DOCKER: bool
    DOCKER_DB: str

    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASS: str
    DB_NAME: str

    @property
    def DATABASE_URL_asyncpg(self):
        """Config a link to database connection for asyncpg."""
        # postgresql+asyncpg://postgres:postgres@localhost:5432/db_name
        if self.DOCKER:
            return (
                "postgresql+asyncpg://"
                f"{self.DB_USER}:{self.DB_PASS}@"
                f"{self.DOCKER_DB}/{self.DB_NAME}"
            )
        return (
            "postgresql+asyncpg://"
            f"{self.DB_USER}:{self.DB_PASS}@"
            f"{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
        )

    model_config = SettingsConfigDict(env_file="app/.env", extra='allow')


db_settings = DBSettings()
