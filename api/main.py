import random

import fastapi
from fastapi import HTTPException

app = fastapi.FastAPI()

@app.get("/generate_name")
async def generate_name(starts_with:str='n', ends_with:str='a'):
    names = ["Minnie", "Margaret", "Malala", "Moana", "Myrtle", "Noa", "Nadia"]
    if starts_with:
        names = [n for n in names if n.lower().startswith(starts_with)]
    if ends_with:
        names = [n for n in names if n.lower().endswith(ends_with)]
    if len(names) == 0:
        raise HTTPException(status_code=404, detail="No names found")
    random_name = random.choice(names)
    return {"name": random_name}
    