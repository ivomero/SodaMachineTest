import unittest
from wallet import Wallet


class TestWallet(unittest.TestCase):

    def setUp(self):
        self.wallet = Wallet()

    def test_wallet_length(self):
        """Test to see if the wallet money list is equal to 88"""
        self.assertEqual(len(self.wallet.money), 88)


if __name__ == '__main__':
    unittest.main()
