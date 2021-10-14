import unittest
from SodaMachineTest.SodaMachineTest.cans import Cola
from soda_machine import SodaMachine
from cans import OrangeSoda
from coins import Nickel, Quarter, Dime, Penny


class TestSodaMachine(unittest.TestCase):
    def setUp(self):
        self.soda_machine = SodaMachine()

    def test_get_coin_from_register_quarter(self):
        """Check that you can retrieve quarter from the register"""
        coin = self.soda_machine.get_coin_from_register(Quarter)
        self.assertEqual(coin.name, Quarter)

    def test_get_coin_from_register_dime(self):
        """Check that you can retrieve Dime from the register"""
        coin = self.soda_machine.get_coin_from_register(Dime)
        self.assertEqual(coin.name, Dime)

    def test_get_coin_from_register_nickel(self):
        """Check that you can retrieve Nickel from the register"""
        coin = self.soda_machine.get_coin_from_register(Nickel)
        self.assertEqual(coin.name, Nickel)

    def test_get_coin_from_register_penny(self):
        """Check that you can retrieve Penny from the register"""
        coin = self.soda_machine.get_coin_from_register(Penny)
        self.assertEqual(coin.name, Penny)

    def test_get_coin_from_register_invalid(self):
        """Check that you can return 'None' from the register"""
        coin = self.soda_machine.get_coin_from_register("Half Dollar")
        self.assertEqual(coin, None)

    def test_get_back_dime(self):
        """Check that you can return dime back from the register"""
        coin = self.soda_machine.get_coin_from_register(Dime)
        self.assertEqual(coin.name, Dime)

    def test_get_back_nickel(self):
        """Check that you can return nickel from the register"""
        coin = self.soda_machine.get_coin_from_register(Nickel)
        self.assertEqual(coin.name, Nickel)

    def test_get_back_penny(self):
        """Check that you can return penny from the register"""
        coin = self.soda_machine.get_coin_from_register(Penny)
        self.assertEqual(coin.name, Penny)

    def test_get_back_quarter(self):
        """Check that you can return from the register"""
        coin = self.soda_machine.get_coin_from_register(Quarter)
        self.assertEqual(coin.name, Quarter)

    def test_fill_register(self):
        """Test that the register has a length of 88"""
        self.assertEqual(len(self.soda_machine.register), 88)

    def test_fill_inventory(self):
        """Test that inventory has a length of 30"""
        self.assertEqual(len(self.soda_machine.inventory), 30)

    def test_get_inventory_soda_cola(self):
        """Ensure that name of soda passed in returns same name"""
        can = self.soda_machine.get_inventory_soda(Cola)
        self.assertEqual(can.name, Cola)

    def test_get_inventory_soda_orange_soda(self):
        """Ensure that name of soda passed in returns same name"""
        can = self.soda_machine.get_inventory_soda('Orange Soda')
        self.assertEqual(can.name, 'Orange Soda')

    def test_get_inventory_soda_root_beer(self):
        """Ensure that name of soda passed in returns same name"""
        can = self.soda_machine.get_inventory_soda('Root Beer')
        self.assertEqual(can.name, 'Root Beer')

    def test_get_inventory_soda_invalid(self):
        """Ensure that name of soda not in selection options passed in returns None"""
        can = self.soda_machine.get_inventory_soda('Mounatin Dew')
        self.assertEqual(can, None)

    def test_return_inventory(self):
        """Add a can and retest inventory length. It should now be 31"""
        can = OrangeSoda()
        self.soda_machine.return_inventory(can)
        self.assertEqual(len(self.soda_machine.inventory), 31)

    def test_deposit_coins_into_register(self):
        """Each of the 4 coins should equal 92 cents"""
        coin_list = [Quarter(), Dime(), Nickel(), Penny()]
        self.soda_machine.deposit_coins_into_register(coin_list)
        self.assertEqual(len(self.soda_machine.register), 92)

    def test_determine_change_value (self):
        """Determine if coins hold correct value"""
        change = self.soda_machine.determine_change_value(0.60, 0.60)
        self.assertEqual(change, 0)

    def test_determine_payment_higher (self):
        """Check if coin value stays true when coin value is more than soda"""
        change = self.soda_machine.determine_change_value(0.80, 0.60)
        self.assertEqual(change, 0.20)

    def test_determine_sod_price_higher (self):
        """Check if coin value stays true when price of soda is more than change input"""
        change = self.soda_machine.determine_change_value(0.60, 0.90)
        self.assertEqual(change, -0.30)

    def test_calculate_coin_value(self):
        """Check coin value by adding them up. Sum should be .41"""
        coin_list = [Quarter(), Dime(), Nickel(), Penny()]
        coin_list_final = self.soda_machine.calculate_coin_value(coin_list)
        self.assertEqual(coin_list_final, .41)

    def test_calculate_coin_value_empty(self):
        """Test that empy input of coins will return 0"""
        coin_list = []
        coin_list_final = self.soda_machine.calculate_coin_value(coin_list)
        self.assertEqual(coin_list_final, 0)



if __name__ == '__main__':
    unittest.main()
