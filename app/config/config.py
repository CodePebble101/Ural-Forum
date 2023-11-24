from os import environ
from dotenv import load_dotenv

load_dotenv()


class DefaultServerSettings:
    ENV: str = environ.get("ENV", "local")
    PATH_PREFIX: str = environ.get("PATH_PREFIX", "/ural/api/v1")
    APP_HOST: str = environ.get("APP_HOST", "0.0.0.0")
    APP_PORT: int = int(environ.get("APP_PORT", 10090))

MONGO_URL: str = environ.get("MONGO_URL")