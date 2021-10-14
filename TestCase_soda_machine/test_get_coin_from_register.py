import unittest
from coins import Coin
from soda_machine import SodaMachine
from SodaMachineTest.coins import Dime, Nickel, Penny, Quarter

class TestReturnCoin(unittest.TestCase):
    
    def setUp(self)-> None:
        self.soda_machine = SodaMachine

    def test_get_coin_from_register(self):
        self.assertEqual(SodaMachine.get_coin_from_register, Quarter)

    def test_get_back_dime(self):
        self.assertEqual(SodaMachine.get_coin_from_register, Dime)

    def test_get_back_nickel(self):
        self.assertEqual(SodaMachine.get_coin_from_register, Nickel)
    
    def test_get_back_penny(self):
        self.assertEqual(SodaMachine.get_coin_from_register, Penny)

    def test_get_back_quarter(self):
        self.assertNotEqual(SodaMachine.get_coin_from_register, "")

if __name__ == '__main__':
    unittest.main()