import unittest
from SodaMachineTest.cans import Cola, OrangeSoda, RootBeer
from soda_machine import SodaMachine


class TestFillRegister(unittest.TestCase):
    """Test for SodaMachine's fill_register"""

    def setUp(self) -> None:
        self.soda_machine = SodaMachine

    def test_fill_inventory(self):
        number_of_cans = self.assertEqual(len(SodaMachine.fill_inventory, 30))
        return number_of_cans


if __name__ == '__main__':
    unittest.main()
