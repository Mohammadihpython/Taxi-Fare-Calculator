from pydantic_settings import BaseSettings


class Config(BaseSettings):
    VALHALLA_URL ="localhost:8002"


    class config:
        env_file = ".env"