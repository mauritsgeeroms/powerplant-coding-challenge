
from fastapi import FastAPI
from basemodel import ProductionInput
from engine import engine


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/productionplan")
async def create_item(item: ProductionInput):
    engine_instance = engine(item)
    return engine_instance.calculate_consumption()