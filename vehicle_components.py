import unittest
from your_module import SpindlerBattery, CarriganTires, OctoprimeTires

class TestSpindlerBattery(unittest.TestCase):
    def test_battery_service(self):
        battery = SpindlerBattery(years_used=3)
        self.assertEqual(battery.needs_service(), True)

class TestCarriganTires(unittest.TestCase):
    def test_tire_service(self):
        tires = CarriganTires([0.9, 0.8, 0.8, 0.8])
        self.assertEqual(tires.needs_service(), True)

class TestOctoprimeTires(unittest.TestCase):
    def test_tire_service(self):
        tires = OctoprimeTires([0.9, 0.9, 0.9, 0.9])
        self.assertEqual(tires.needs_service(), True)

if __name__ == '__main__':
    unittest.main()
