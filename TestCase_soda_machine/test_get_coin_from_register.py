import unittest
from coins import Coin
from soda_machine import SodaMachine
from SodaMachineTest.coins import Dime, Nickel, Penny, Quarter

class TestReturnCoin:
    
    def setUp(self)-> None:
        self.soda_machine = SodaMachine

    def test_get_coin_from_register(self):
        quarter_back = self.assertEqual(len(SodaMachine.get_coin_from_register.register.remove, "Quarter"))
        return quarter_back

    def test_get_back_dime(self):
        self.assertTrue(SodaMachine.get_coin_from_register.name, "Dime"))

    def test_get_back_nickel(self):
        self.assertEqual(len(SodaMachine.get_coin_from_register.name, "Nickel"))

    def test_get_back_penny(self):
        self.assertEqual(len(SodaMachine.get_coin_from_register.name, "Penny"))

    def test_get_back_quarter(self):
        self.assertNotEqual(len(SodaMachine.get_coin_from_register.coin_name, ""))

if __name__ == '__main__':
    unittest.main()