from abc import ABC, abstractmethod

class Engine(ABC):

    @abstractmethod
    def needs_service(self) -> bool:
        pass

class WilloughbyEngine(Engine):

    def __init__(self, current_mileage, last_service_mileage):
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def needs_service(self):
        if self.last_service_mileage + 60000 < self.current_mileage:
            return True
        else:
            return False

class CapuletEngine(Engine):
    
        def __init__(self, current_mileage, last_service_mileage):
            self.current_mileage = current_mileage
            self.last_service_mileage = last_service_mileage
    
        def needs_service(self):
            if self.last_service_mileage + 30000 < self.current_mileage:
                return True
            else:
                return False

class SternmanEngine(Engine):
    
        def __init__(self, warning_light):
            self.warning_light = warning_light
    
        def needs_service(self):
            if self.warning_light:
                return True
            else:
                return False
