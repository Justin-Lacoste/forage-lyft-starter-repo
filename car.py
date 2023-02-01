from abc import ABC, abstractmethod
from datetime import datetime
from engine import CapuletEngine
from engine import WilloughbyEngine
from engine import SternmanEngine
from battery import SpindlerBattery
from battery import NubbinBattery


class Serviceable(ABC):
    @abstractmethod
    def needs_service(self) -> bool:
        pass

class Car(Serviceable):
    def __init__(self, engine, battery):
        self.engine = engine
        self.battery = battery

    def needs_service(self) -> bool:
        return self.engine.needs_service() or self.battery.needs_service()

class CarFactory:

    @staticmethod
    def create_calliope(current_date, last_serviced, current_mileage, last_service_mileage) -> Car:
        engine = CapuletEngine(last_service_mileage, current_mileage)
        battery = SpindlerBattery(last_serviced, current_date)
        return Car(engine, battery)

    @staticmethod
    def create_glissade(current_date, last_serviced, current_mileage, last_service_mileage) -> Car:
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        battery = SpindlerBattery(last_serviced, current_date)
        return Car(engine, battery)

    @staticmethod
    def create_palindrome(current_date, last_serviced, warning_light_on) -> Car:
        engine = SternmanEngine(warning_light_on)
        battery = SpindlerBattery(last_serviced, current_date)
        return Car(engine, battery)

    @staticmethod
    def create_thovex(current_date, last_serviced, current_mileage, last_service_mileage) -> Car:
        engine = CapuletEngine(last_service_mileage, current_mileage)
        battery = NubbinBattery(last_serviced, current_date)
        return Car(engine, battery)

    @staticmethod
    def create_glissade(current_date, last_serviced, current_mileage, last_service_mileage) -> Car:
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        battery = NubbinBattery(last_serviced, current_date)
        return Car(engine, battery)


