import unittest
from soda_machine import SodaMachine


class TestGetInventorySoda(unittest.TestCase):
    def setup(self):
        self.soda_machine = SodaMachine()

    def test_get_inventory_soda(self):
        can = self.soda_machine.get_inventory_soda('Cola')
        self.assertEqual(can, 'Cola')


if __name__ == '__main__':
    unittest.main()
