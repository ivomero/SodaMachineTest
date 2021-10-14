import unittest
from soda_machine import SodaMachine
from cans import OrangeSoda
from coins import Nickel, Quarter, Dime, Penny


class TestSodaMachine(unittest.TestCase):
    def setUp(self):
        self.soda_machine = SodaMachine()

    def test_get_coin_from_register_quarter(self):
        coin = self.soda_machine.get_coin_from_register("Quarter")
        self.assertEqual(coin.name, "Quarter")

    def test_get_coin_from_register_dime(self):
        coin = self.soda_machine.get_coin_from_register("Dime")
        self.assertEqual(coin.name, "Dime")

    def test_get_coin_from_register_nickel(self):
        coin = self.soda_machine.get_coin_from_register("Nickel")
        self.assertEqual(coin.name, "Nickel")

    def test_get_coin_from_register_penny(self):
        coin = self.soda_machine.get_coin_from_register("Penny")
        self.assertEqual(coin.name, "Penny")

    def test_get_coin_from_register_invalid(self):
        coin = self.soda_machine.get_coin_from_register("Half Dollar")
        self.assertEqual(coin, None)

    def test_get_back_dime(self):
        coin = self.soda_machine.get_coin_from_register("Dime")
        self.assertEqual(coin.name, "Dime")

    def test_get_back_nickel(self):
        coin = self.soda_machine.get_coin_from_register("Nickel")
        self.assertEqual(coin.name, "Nickel")

    def test_get_back_penny(self):
        coin = self.soda_machine.get_coin_from_register("Penny")
        self.assertEqual(coin.name, "Penny")

    def test_get_back_quarter(self):
        coin = self.soda_machine.get_coin_from_register("Quarter")
        self.assertEqual(coin.name, "Quarter")

    def test_fill_register(self):
        self.assertEqual(len(self.soda_machine.register), 88)

    def test_fill_inventory(self):
        self.assertEqual(len(self.soda_machine.inventory), 30)

    def test_get_inventory_soda_cola(self):
        can = self.soda_machine.get_inventory_soda('Cola')
        self.assertEqual(can.name, 'Cola')

    def test_get_inventory_soda_orange_soda(self):
        can = self.soda_machine.get_inventory_soda('Orange Soda')
        self.assertEqual(can.name, 'Orange Soda')

    def test_get_inventory_soda_root_beer(self):
        can = self.soda_machine.get_inventory_soda('Root Beer')
        self.assertEqual(can.name, 'Root Beer')

    def test_get_inventory_soda_invalid(self):
        can = self.soda_machine.get_inventory_soda('Mounatin Dew')
        self.assertEqual(can, None)

    def test_return_inventory(self):
        can = OrangeSoda()
        self.soda_machine.return_inventory(can)
        self.assertEqual(len(self.soda_machine.inventory), 31)

    def test_deposit_coins_into_register(self):
        coin_list = [Quarter(), Dime(), Nickel(), Penny()]
        self.soda_machine.deposit_coins_into_register(coin_list)
        self.assertEqual(len(self.soda_machine.register), 92)


if __name__ == '__main__':
    unittest.main()
