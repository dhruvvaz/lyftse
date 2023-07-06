import unittest
from car import Thovex
from battery import Nubbin

class TestCarMethods(unittest.TestCase):

    def setUp(self):
        self.car = Thovex("ModelName", Nubbin())

    def test_car_model(self):
        self.assertEqual(self.car.model, "ModelName", "Car model name does not match")

    def test_car_battery(self):
        self.assertIsInstance(self.car.battery, Nubbin, "Car battery type does not match")

class TestBatteryMethods(unittest.TestCase):

    def setUp(self):
        self.battery = Nubbin()

    def test_battery_type(self):
        self.assertEqual(self.battery.get_battery_type(), "Nubbin", "Battery type does not match")

    def test_battery_range(self):
        self.assertEqual(self.battery.get_range(), 200, "Battery range does not match")

if __name__ == '__main__':
    unittest.main()
