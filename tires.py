from abc import ABC, abstractmethod

class Tires(ABC):
    
    @abstractmethod
    def needs_service(self) -> bool:
        pass

class CarriganTires(Tires):

    def __init__(self, tire_wear: list):
        self.tire_wear = tire_wear

    def needs_service(self):
        change_required = False
        for tire in self.tire_wear:
            if tire >= 0.9:
                change_required = True
        return change_required


class OctoprimeTires(Tires):

    def __init__(self, tire_wear: list):
        self.tire_wear = tire_wear

    def needs_service(self):
        return sum(self.tire_wear) >= 3
