import unittest
from datetime import datetime

from engine import WilloughbyEngine, CapuletEngine, SternmanEngine
from battery import SpindlerBattery, NubbinBattery


class TestBattery(unittest.TestCase):
    
        def test_spindler_battery_needs_service(self):
            spindler_battery = SpindlerBattery(datetime(2018, 1, 1), datetime(2020, 1, 1))
            self.assertTrue(spindler_battery.needs_service())

        def test_spindler_battery_no_need_for_service(self):
            spindler_battery = SpindlerBattery(datetime(2018, 1, 1), datetime(2019, 12, 31))
            self.assertFalse(spindler_battery.needs_service())
    
        def test_nubbin_battery_needs_service(self):
            nubbin_battery = NubbinBattery(datetime(2018, 1, 1), datetime(2022, 1, 1))
            self.assertTrue(nubbin_battery.needs_service())

        def test_spindler_battery_no_need_for_service(self):
            nubbin_battery = NubbinBattery(datetime(2018, 1, 1), datetime(2020, 1, 1))
            self.assertFalse(nubbin_battery.needs_service())

class TestEngine(unittest.TestCase):
        
            def test_willoughby_engine_needs_service(self):
                willoughby_engine = WilloughbyEngine(100, 65000)
                self.assertTrue(willoughby_engine.needs_service())

            def test_willoughby_engine_no_need_for_service(self):
                willoughby_engine = WilloughbyEngine(1000, 2000)
                self.assertFalse(willoughby_engine.needs_service())

            def test_capulet_engine_needs_service(self):
                capulet_engine = CapuletEngine(100, 35000)
                self.assertTrue(capulet_engine.needs_service())
            
            def test_capulet_engine_no_need_for_service(self):
                capulet_engine = CapuletEngine(1000, 2000)
                self.assertFalse(capulet_engine.needs_service())

            def test_sternman_engine_needs_service(self):
                sternman_engine = SternmanEngine(True)
                self.assertTrue(sternman_engine.needs_service())

            def test_sternman_engine_no_need_for_service(self):
                sternman_engine = SternmanEngine(False)
                self.assertFalse(sternman_engine.needs_service())

if __name__ == '__main__':
    unittest.main()
