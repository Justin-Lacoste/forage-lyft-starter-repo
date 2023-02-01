from abc import ABC, abstractmethod
from datetime import datetime

class Battery(ABC):

    @abstractmethod
    def needs_service(self) -> bool:
        pass

class SpindlerBattery(Battery):

    def __init__(self, last_service_date, current_date):
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self):
        if self.last_service_date.replace(year=self.last_service_date.year + 3) < self.current_date:
            return True
        else:
            return False

class NubbinBattery(Battery):

    def __init__(self, last_service_date, current_date):
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self):
        
        if self.last_service_date.replace(year=self.last_service_date.year + 4) < self.current_date:
            return True
        else:
            return False
