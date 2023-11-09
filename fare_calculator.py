import json
from turtle import distance
from fastapi import FastAPI
from pydantic import BaseModel
import httpx
from .config import Config
import json

app = FastAPI()


settings = Config()
class Coordinates(BaseModel):
    lat:float
    lon:float


@app.post("/taxi-fare")
async def computing_fare(start:Coordinates,destination:Coordinates):
    # calculate distance and duration using valhalla service
    async with httpx.AsyncClient() as client:
        data ={
            "locations":[start.model_dump(),destination.model_dump()],
            "costing":"taxi",
            "direction_options":{
                "units":"kilometers",
            }
        }
        route_response = await client.post(settings.VALHALLA_URL,json=json.dumps(data))
        distance = route_response.json()["trip"]["summary"]["length"]
        duration = route_response.json()["trip"]["summary"]["time"]

        # calculate fare based on distance and duration
        fare = None

        return {"start":start,"destination":destination,"fare":fare}


