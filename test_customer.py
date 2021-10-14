import unittest
from SodaMachineTest.SodaMachineTest.cans import Cola
from SodaMachineTest.SodaMachineTest.coins import Dime, Nickel, Penny, Quarter
from customer import Customer


class TestGetWalletCoin(unittest.TestCase):
    """Tests for Customer's get_wallet_coin method"""

    def setUp(self):
        self.customer = Customer()

    def test_can_return_quarter(self):
        """Pass in 'Quarter', method should return a Quarter instance"""
        returned_coin = self.customer.get_wallet_coin(Quarter)
        self.assertEqual(returned_coin.value, .25)

    def test_can_return_dime(self):
        """Pass in 'Dime', method should return a Dime instance"""
        returned_coin = self.customer.get_wallet_coin(Dime)
        self.assertEqual(returned_coin.value, .10)

    def test_can_return_nickel(self):
        """Pass in 'Nickel', method should return a Nickel instance"""
        returned_coin = self.customer.get_wallet_coin(Nickel)
        self.assertEqual(returned_coin.value, .05)

    def test_can_return_penny(self):
        """Pass in 'Penny', method should return a Penny instance"""
        returned_coin = self.customer.get_wallet_coin(Penny)
        self.assertEqual(returned_coin.value, .01)

    def test_valid_input(self):
        """Test if an input is invalid, method should return None"""
        returned_coin = self.customer.get_wallet_coin('Half Dollar')
        self.assertNotEqual(returned_coin, .25)

    def test_add_coin_list_to_wallet(self):
        """ Pass in list of coins, method should show the Customer's Money's Wallet List grow by 3"""
        coins = [Quarter, Dime, Penny]
        self.customer.add_coins_to_wallet(coins)
        self.assertEqual(len(self.customer.wallet.money), 91)

    def test_empty_coin_list_to_wallet(self):
        """ Pass in an empty list of coins, method should show the amount of coints remains the same"""
        coins = []
        self.customer.add_coins_to_wallet(coins)
        self.assertEqual(len(self.customer.wallet.money), 88)

    def test_add_can_to_back_pack(self):
        """Pass in a Cola Object, method Customer's Backpack's purchased_can's list grow by 1"""
        soda = Cola
        self.customer.add_can_to_backpack(soda)
        self.assertEqual(len(self.customer.backpack.purchased_cans), 1)


if __name__ == '__main__':
    unittest.main()
