from typing import Any, List
from pydantic import BaseModel

class Fuels(BaseModel):
    name: str
    type: str
    efficiency: float
    pmin: int
    pmax: int

class ProductionInput(BaseModel):
    load: int
    fuels: Any
    powerplants: List[Fuels]
