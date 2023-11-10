from fastapi import FastAPI,status, HTTPException
from pydantic import BaseModel
import httpx
from config import Config

app = FastAPI()


settings = Config()
class Coordinates(BaseModel):
    lat:float
    lon:float


@app.post("/taxi-fare",status_code=status.HTTP_200_OK)
async def computing_fare(start:Coordinates,destination:Coordinates):
    # calculate distance and duration using valhalla service
    try:
        async with httpx.AsyncClient() as client:
            data ={
                "locations":[start.model_dump(),destination.model_dump()],
                "costing":"auto",
                "costing_options":{"auto":{"country_crossing_penalty":2000.0}},
                "units":"kilometers",
                "id":"my_work_route"
            }
            url = f"{settings.VALHALLA_URL}/route"
            response = await client.post(url,json=data)
            response.raise_for_status()
            distance = response.json()["trip"]["summary"]["length"]
            duration = response.json()["trip"]["summary"]["time"]

            # calculate fare based on distance and duration
            fare = settings.BASE_FARE + (settings.COST_PER_KM * distance) + (settings.COST_PER_MINUTE * (duration / 60))

            return {"start":start,"destination":destination,"fare":fare}
    except httpx.HTTPError as e:
            raise HTTPException(status.HTTP_400_BAD_REQUEST,detail=f"invalid coordinate or {e}" )
    except Exception as e:
            raise HTTPException(status.HTTP_400_BAD_REQUEST,detail=f"{e}")

