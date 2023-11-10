from pprint import pprint
import httpx
import asyncio
async def get_rout():
    url ="http://vallhalla:8002/route"

    json_payload ={
        "locations":[
            {"lat":36.324,"lon":59.744},
            {"lat":35.8839,"lon":50.9570}
            ],"costing":"auto"
        ,"costing_options":{"auto":{"country_crossing_penalty":2000.0}},
        "units":"kilometers",
        "id":"my_work_route"
        }

    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(url,json=json_payload)
            response.raise_for_status()
            pprint(response.json()["trip"]["summary"])
        except httpx.HTTPError as e:
            print(f"HTTP error occurred:{e}")
        except Exception as e:
            print(f"An error occurred:{e}")

asyncio.run(get_rout())