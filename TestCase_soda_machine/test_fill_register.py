import unittest
from SodaMachineTest.coins import Dime, Nickel, Penny, Quarter
from soda_machine import SodaMachine
from coins import Coin

class TestFillRegister(unittest.TestCase):
    """Test for SodaMachine's fill_register"""

    def setUp(self) -> None:
        self.soda_machine = SodaMachine()
        
    def test_fill_register(self):
        number_of_coins = self.assertEqual(len(SodaMachine.fill_register, 80))
        return number_of_coins

if __name__ == '__main__':
    unittest.main()
