from pydantic_settings import BaseSettings


class Config(BaseSettings):
    VALHALLA_URL :str="http://localhost:8002"
    BASE_FARE: float=2000
    COST_PER_KM: float=2000
    COST_PER_MINUTE:float=1000


    class config:
        env_file = ".env"