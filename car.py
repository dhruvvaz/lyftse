from engine import Engine
from battery import Battery

class Car:
    def __init__(self, model, last_service_date, current_mileage, last_service_mileage, warning_light_is_on):
        self.model = model
        if model in ["Calliope", "Thovex"]:
            self.part = Engine(last_service_date, current_mileage, last_service_mileage)
        elif model in ["Glissade", "Rorschach"]:
            self.part = Battery(last_service_date, warning_light_is_on)

    def needs_service(self):
        return self.part.needs_service()
