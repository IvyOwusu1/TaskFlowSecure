from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # -------------------------
    # Application Settings
    # -------------------------
    APP_NAME: str = "TaskFlow Secure"
    APP_VERSION: str = "0.1.0"
    DEBUG: bool = True

    # -------------------------
    # Database Settings
    # -------------------------
    DATABASE_HOST: str
    DATABASE_PORT: int
    DATABASE_NAME: str
    DATABASE_USER: str
    DATABASE_PASSWORD: str

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )

    @property
    def DATABASE_URL(self) -> str:
        return (
            f"postgresql+psycopg://"
            f"{self.DATABASE_USER}:"
            f"{self.DATABASE_PASSWORD}@"
            f"{self.DATABASE_HOST}:"
            f"{self.DATABASE_PORT}/"
            f"{self.DATABASE_NAME}"
        )


settings = Settings()