from basemodel import ProductionInput
import json

class engine:

    def __init__(self, production_input: ProductionInput):
        self.production_input = production_input
        self.mapping_type = {
            "gasfired": "gas(euro/MWh)",
            "turbojet": "kerosine(euro/MWh)",
            "windturbine": "wind(%)"
        }

    def _get_merit_indices(self, costs, powerplants, fuels):
        merit_index = [{
            "index": costs[powerplant.type]/powerplant.efficiency,
            "p": powerplant.pmax if powerplant.type != "windturbine" else powerplant.pmax*fuels["wind(%)"]*0.01,
            "pmin": powerplant.pmin,
            "name": powerplant.name} for powerplant in powerplants]
        merit_index.sort(key=lambda x: x["index"])
        return merit_index

    def calculate_consumption(self):
        fuels = self.production_input.fuels

        costs = {
            "gasfired": float(fuels[self.mapping_type['gasfired']]),
            "turbojet": float(fuels[self.mapping_type['turbojet']]),
            "windturbine": 0
        }

        powerplants = self.production_input.powerplants

        load = self.production_input.load

        merit_index = self._get_merit_indices(costs, powerplants, fuels)

        response = []
        for item in merit_index:
            
            response.append({
                "name": item["name"],
                "p": item["p"] if load > item["p"] else (max(load, item["pmin"]) if load > 0 else 0.0)
            })
            load -= item["p"]
        return response

