class SpindlerBattery(Battery):
    def __init__(self, years_used):
        self.years_used = years_used

    def needs_service(self):
        return self.years_used >= 3

class CarriganTires(Tires):
    def __init__(self, wear):
        self.wear = wear

    def needs_service(self):
        return max(self.wear) >= 0.9

class OctoprimeTires(Tires):
    def __init__(self, wear):
        self.wear = wear

    def needs_service(self):
        return sum(self.wear) >= 3
