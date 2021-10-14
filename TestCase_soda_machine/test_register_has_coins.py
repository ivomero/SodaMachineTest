import unittest
from coins import Coin
from soda_machine import SodaMachine
from SodaMachineTest.coins import Dime, Nickel, Penny, Quarter

class RegisterHasCoin(unittest.TestCase):
    def setUp(self) -> None:
        self.soda_machine = SodaMachine

    def test_register_has_coin(self):
        is_coin_there = self.assertTrue(SodaMachine.register_has_coin)
        return is_coin_there
        

if __name__ == '__main__':
    unittest.main()