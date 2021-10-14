import unittest
from customer import Customer
from wallet import Wallet
from soda_machine import SodaMachine
from cans import OrangeSoda
from coins import Nickel, Quarter, Dime, Penny
from user_interface import display_payment_value, get_unique_can_names, try_parse_int, validate_coin_selection, validate_main_menu
from cans import Cola, OrangeSoda, RootBeer


class TestGetWalletCoin(unittest.TestCase):
    """Tests for Customer's get_wallet_coin method"""

    def setUp(self):
        self.customer = Customer()

    def test_can_return_quarter(self):
        """Pass in 'Quarter', method should return a Quarter instance"""
        returned_coin = self.customer.get_wallet_coin('Quarter')
        self.assertEqual(returned_coin.value, .25)

    def test_can_return_dime(self):
        """Pass in 'Dime', method should return a Dime instance"""
        returned_coin = self.customer.get_wallet_coin('Dime')
        self.assertEqual(returned_coin.value, .10)

    def test_can_return_nickel(self):
        """Pass in 'Nickel', method should return a Nickel instance"""
        returned_coin = self.customer.get_wallet_coin('Nickel')
        self.assertEqual(returned_coin.value, .05)

    def test_can_return_penny(self):
        """Pass in 'Penny', method should return a Penny instance"""
        returned_coin = self.customer.get_wallet_coin('Penny')
        self.assertEqual(returned_coin.value, .01)

    def test_valid_input(self):
        """Test if an input is invalid, method should return None"""
        returned_coin = self.customer.get_wallet_coin('Half Dollar')
        self.assertNotEqual(returned_coin, .25)

    def test_add_coin_list_to_wallet(self):
        """ Pass in list of coins, method should show the Customer's Money's Wallet List grow by 3"""
        coins = ['Quarter', 'Dime', 'Penny']
        self.customer.add_coins_to_wallet(coins)
        self.assertEqual(len(self.customer.wallet.money), 91)

    def test_empty_coin_list_to_wallet(self):
        """ Pass in an empty list of coins, method should show the amount of coints remains the same"""
        coins = []
        self.customer.add_coins_to_wallet(coins)
        self.assertEqual(len(self.customer.wallet.money), 88)

    def test_add_can_to_back_pack(self):
        """Pass in a Cola Object, method Customer's Backpack's purchased_can's list grow by 1"""
        soda = "Cola"
        self.customer.add_can_to_backpack(soda)
        self.assertEqual(len(self.customer.backpack.purchased_cans), 1)


class TestUserInterface(unittest.TestCase):

    def test_validate_main_menu_1(self):
        """Test to see if 1 is = True, 1"""
        selection = validate_main_menu(1)
        self.assertEqual(selection, (True, 1))

    def test_validate_main_menu_2(self):
        """Test to see if 2 is = True, 2"""
        selection = validate_main_menu(2)
        self.assertEqual(selection, (True, 2))

    def test_validate_main_menu_3(self):
        """Test to see if 3 is = True, 3"""
        selection = validate_main_menu(3)
        self.assertEqual(selection, (True, 3))

    def test_validate_main_menu_4(self):
        """Test to see if 4 is = True, 4"""
        selection = validate_main_menu(4)
        self.assertEqual(selection, (True, 4))

    def test_validate_main_menu_invalid(self):
        """Test to see if integer != 1-4 is = False, None"""
        selection = validate_main_menu(5)
        self.assertEqual(selection, (False, None))

    def test_parse_int(self):
        """Test to show parseint working correctly"""
        number = try_parse_int("10")
        self.assertEqual(number, 10)

    def test_parse_int_word(self):
        """Test verifying that entering a word into parseint returns the value of 0"""
        number = try_parse_int("hello")
        self.assertEqual(number, 0)

    def test_get_unique_can_names(self):
        """Test esures that passing in a list of cans will show only unique cans in list"""
        can_list = [OrangeSoda(), OrangeSoda(), Cola(),
                    Cola(), RootBeer(), RootBeer()]
        can_list_final = get_unique_can_names(can_list)
        self.assertEqual(len(can_list_final), 3)

    def test_get_unique_can_names_empty(self):
        """Test ensures that passing in an empty list will show nothing is in list"""
        can_list = []
        can_list_final = get_unique_can_names(can_list)
        self.assertEqual(len(can_list_final), 0)

    def test_display_payment_value(self):
        coin_list = [Quarter(), Dime(), Nickel(), Penny()]
        coin_list_final = display_payment_value(coin_list)
        self.assertEqual(coin_list_final, .41)

    def test_display_payment_value_empty_list(self):
        coin_list = []
        coin_list_final = display_payment_value(coin_list)
        self.assertEqual(coin_list_final, 0)

    def test_valid_coin_selection_1(self):
        """Test to see if integer != 1 is = True, Quarter """
        selection = validate_coin_selection(1)
        self.assertEqual(selection, (True, "Quarter"))

    def test_valid_coin_selection_2(self):
        """Test to see if integer != 2 is = True, "Dime" """
        selection = validate_coin_selection(2)
        self.assertEqual(selection, (True, "Dime"))

    def test_valid_coin_selection_3(self):
        """Test to see if integer != 3 is = True, "Nickel" """
        selection = validate_coin_selection(3)
        self.assertEqual(selection, (True, "Nickel"))

    def test_valid_coin_selection_4(self):
        """Test to see if integer != 4 is = True, "Penny" """
        selection = validate_coin_selection(4)
        self.assertEqual(selection, (True, "Penny"))

    def test_valid_coin_selection_5(self):
        """Test to see if integer != 5 is = True, Done"""
        selection = validate_coin_selection(5)
        self.assertEqual(selection, (True, "Done"))

    def test_valid_coin_selection_invalid(self):
        """Test to see if integer != 1-5 is = False, None"""
        selection = validate_coin_selection(6)
        self.assertEqual(selection, (False, None))


class TestWallet(unittest.TestCase):

    def setUp(self):
        self.wallet = Wallet()

    def test_wallet_length(self):
        """Test to see if the wallet money list is equal to 88"""
        self.assertEqual(len(self.wallet.money), 88)


class TestSodaMachine(unittest.TestCase):
    def setUp(self):
        self.soda_machine = SodaMachine()

    def test_get_coin_from_register_quarter(self):
        """Check that you can retrieve quarter from the register"""
        coin = self.soda_machine.get_coin_from_register("Quarter")
        self.assertEqual(coin.name, "Quarter")

    def test_get_coin_from_register_dime(self):
        """Check that you can retrieve Dime from the register"""
        coin = self.soda_machine.get_coin_from_register("Dime")
        self.assertEqual(coin.name, "Dime")

    def test_get_coin_from_register_nickel(self):
        """Check that you can retrieve Nickel from the register"""
        coin = self.soda_machine.get_coin_from_register("Nickel")
        self.assertEqual(coin.name, "Nickel")

    def test_get_coin_from_register_penny(self):
        """Check that you can retrieve Penny from the register"""
        coin = self.soda_machine.get_coin_from_register("Penny")
        self.assertEqual(coin.name, "Penny")

    def test_get_coin_from_register_invalid(self):
        """Check that you can return 'None' from the register"""
        coin = self.soda_machine.get_coin_from_register("Half Dollar")
        self.assertEqual(coin, None)

    def test_get_back_dime(self):
        """Check that you can return dime back from the register"""
        coin = self.soda_machine.get_coin_from_register("Dime")
        self.assertEqual(coin.name, "Dime")

    def test_get_back_nickel(self):
        """Check that you can return nickel from the register"""
        coin = self.soda_machine.get_coin_from_register("Nickel")
        self.assertEqual(coin.name, "Nickel")

    def test_get_back_penny(self):
        """Check that you can return penny from the register"""
        coin = self.soda_machine.get_coin_from_register("Penny")
        self.assertEqual(coin.name, "Penny")

    def test_get_back_quarter(self):
        """Check that you can return from the register"""
        coin = self.soda_machine.get_coin_from_register("Quarter")
        self.assertEqual(coin.name, "Quarter")

    def test_fill_register(self):
        """Test that the register has a length of 88"""
        self.assertEqual(len(self.soda_machine.register), 88)

    def test_fill_inventory(self):
        """Test that inventory has a length of 30"""
        self.assertEqual(len(self.soda_machine.inventory), 30)

    def test_get_inventory_soda_cola(self):
        """Ensure that name of soda passed in returns same name"""
        can = self.soda_machine.get_inventory_soda('Cola')
        self.assertEqual(can.name, 'Cola')

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

    def test_determine_change_value(self):
        """Determine if coins hold correcrt value"""
        change = self.soda_machine.determine_change_value(0.60, 0.60)
        self.assertEqual(change, 0)

    def test_determine_payment_higher(self):
        """Check if coin value stays true when coin value is more than soda"""
        change = self.soda_machine.determine_change_value(0.80, 0.60)
        self.assertEqual(change, 0.20)

    def test_determine_sod_price_higher(self):
        """Check if coin value stays true when price of soda is more than change input"""
        change = self.soda_machine.determine_change_value(0.60, 0.90)
        self.assertEqual(change, -0.30)

    def test_calculate_coin_value(self):
        """Check coin value by adding them up. Sum should be .41"""
        coin_list = [Quarter(), Dime(), Nickel(), Penny()]
        coin_list_final = self.soda_machine.calculate_coin_value(coin_list)
        self.assertEqual(coin_list_final, .41)

    def test_calculate_coin_value_empty(self):
        """Test that empy input of coins will rreturn 0"""
        coin_list = []
        coin_list_final = self.soda_machine.calculate_coin_value(coin_list)
        self.assertEqual(coin_list_final, 0)


if __name__ == '__main__':
    unittest.main()
