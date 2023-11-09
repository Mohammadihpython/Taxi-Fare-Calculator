import json
from fastapi import FastAPI
from pydantic import BaseModel
import httpx
from config import Config
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
            "costing":"auto",
            "costing_options":{"auto":{"country_crossing_penalty":2000.0}},
            "units":"kilometers",
            "id":"my_work_route"
        }
        url = f"{settings.VALHALLA_URL}/route"
        json_data =json.dumps(data)
        response = await client.post(url,json=data)
        distance = response.json()["trip"]["summary"]["length"]
        duration = response.json()["trip"]["summary"]["time"]

        # calculate fare based on distance and duration
        fare = settings.BASE_FARE + (settings.COST_PER_KM * distance) + (settings.COST_PER_MINUTE * (duration / 60))

        return {"start":start,"destination":destination,"fare":fare}


