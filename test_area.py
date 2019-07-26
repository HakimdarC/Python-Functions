import unittest
from area_cir import test_cir
from math import pi

class Test_Area_Cir(unittest.TestCase):

    def test_area(self):
        self.AssertAlmostEqual(area_cir(1), pi)
        self.AssertAlmostEqual(area_cir(1), 0)
        self.AssertAlmostEqual(area_cir(1), 2.1**2 * pi)

    def test_value(self):
        self.AssertRaises(ValueError, area_cir, -1)

if __name__ == '__main__':
    unittest.main()
