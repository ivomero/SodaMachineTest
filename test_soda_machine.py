import unittest
from soda_machine import SodaMachine


class TestSodaMachine(unittest.TestCase):
    def setUp(self):
        self.soda_machine = SodaMachine()

    def test_get_coin_from_register(self):
        quarter_back = self.assertEqual(
            len(SodaMachine.get_coin_from_register.register.remove, "Quarter"))
        return quarter_back

    def test_get_back_dime(self):
        self.assertEqual(SodaMachine.get_coin_from_register.name, "Dime")

    def test_get_back_nickel(self):
        self.assertEqual(
            len(SodaMachine.get_coin_from_register.name, "Nickel"))

    def test_get_back_penny(self):
        self.assertEqual(len(SodaMachine.get_coin_from_register.name, "Penny"))

    def test_get_back_quarter(self):
        self.assertNotEqual(
            len(SodaMachine.get_coin_from_register.coin_name, ""))

    def test_fill_register(self):
        number_of_coins = self.assertEqual(len(SodaMachine.fill_register, 80))
        return number_of_coins

    def test_fill_inventory(self):
        number_of_cans = self.assertEqual(len(SodaMachine.fill_inventory, 30))
        return number_of_cans

    def test_get_inventory_soda(self):
        can = self.soda_machine.get_inventory_soda('Cola')
        self.assertEqual(can, 'Cola')


if __name__ == '__main__':
    unittest.main()
