import unittest
from user_interface import display_payment_value, get_unique_can_names, try_parse_int, validate_coin_selection, validate_main_menu
from cans import Cola, OrangeSoda, RootBeer
from coins import Dime, Nickel, Penny, Quarter


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


if __name__ == '__main__':
    unittest.main()
