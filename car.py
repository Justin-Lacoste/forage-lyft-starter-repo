from abc import ABC, abstractmethod
from datetime import datetime
from engine import CapuletEngine
from engine import WilloughbyEngine
from engine import SternmanEngine
from battery import SpindlerBattery
from battery import NubbinBattery
from tires import CarriganTires
from tires import OctoprimeTires


class Serviceable(ABC):
    @abstractmethod
    def needs_service(self) -> bool:
        pass

class Car(Serviceable):
    def __init__(self, engine, battery, tires):
        self.engine = engine
        self.battery = battery
        self.tires = tires

    def needs_service(self) -> bool:
        return self.engine.needs_service() or self.battery.needs_service()

class CarFactory:

    @staticmethod
    def create_calliope(current_date, last_serviced, current_mileage, last_service_mileage, tire_wear) -> Car:
        engine = CapuletEngine(last_service_mileage, current_mileage)
        battery = SpindlerBattery(last_serviced, current_date)
        tires = CarriganTires(tire_wear)
        return Car(engine, battery, tires)

    @staticmethod
    def create_glissade(current_date, last_serviced, current_mileage, last_service_mileage, tire_wear) -> Car:
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        battery = SpindlerBattery(last_serviced, current_date)
        tires = OctoprimeTires(tire_wear)
        return Car(engine, battery, tires)

    @staticmethod
    def create_palindrome(current_date, last_serviced, warning_light_on, tire_wear) -> Car:
        engine = SternmanEngine(warning_light_on)
        battery = SpindlerBattery(last_serviced, current_date)
        tires = CarriganTires(tire_wear)
        return Car(engine, battery, tires)

    @staticmethod
    def create_thovex(current_date, last_serviced, current_mileage, last_service_mileage, tire_wear) -> Car:
        engine = CapuletEngine(last_service_mileage, current_mileage)
        battery = NubbinBattery(last_serviced, current_date)
        tires = CarriganTires(tire_wear)
        return Car(engine, battery, tires)

    @staticmethod
    def create_glissade(current_date, last_serviced, current_mileage, last_service_mileage, tire_wear) -> Car:
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        battery = NubbinBattery(last_serviced, current_date)
        tires = OctoprimeTires(tire_wear)
        return Car(engine, battery)


