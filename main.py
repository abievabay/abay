from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from utils import generate_calendar

app = FastAPI()

class DateList(BaseModel):
    dates: List[str]

@app.post("/calendar")
def get_calendar(data: DateList):
    try:
        result = generate_calendar(data.dates)
        return {"calendar": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
