<<<<<<< HEAD
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    BOT_TOKEN: str = "8744716076:AAGdf8mHiY9lpwEDbqqqtBJ6jiRhUxKWEfs"
    WEBAPP_URL: str = "http://localhost:5173"
    BACKEND_URL: str = "http://localhost:8000"
    DATABASE_URL: str = "postgresql+asyncpg://postgres.fsruimuuizibgxxwacfh:aqjJTcuuIePgdbXx@aws-0-us-east-1.pooler.supabase.com:6543/postgres"
    ADMIN_TELEGRAM_IDS: str = "5578558407"

    @property
    def admin_ids(self) -> list[int]:
        return [int(x) for x in self.ADMIN_TELEGRAM_IDS.split(",") if x.strip()]

    class Config:
        env_file = ".env"
        extra = "ignore"


=======
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    BOT_TOKEN: str = "8744716076:AAGdf8mHiY9lpwEDbqqqtBJ6jiRhUxKWEfs"
    WEBAPP_URL: str = "http://localhost:5173"
    BACKEND_URL: str = "http://localhost:8000"
    DATABASE_URL: str = "postgresql+asyncpg://postgres.fsruimuuizibgxxwacfh:aqjJTcuuIePgdbXx@aws-0-us-east-1.pooler.supabase.com:6543/postgres"
    ADMIN_TELEGRAM_IDS: str = "5578558407"

    @property
    def admin_ids(self) -> list[int]:
        return [int(x) for x in self.ADMIN_TELEGRAM_IDS.split(",") if x.strip()]

    class Config:
        env_file = ".env"
        extra = "ignore"


>>>>>>> 8cd8cd6ae22d7b25daeee3d119f1400c35df92cb
settings = Settings()