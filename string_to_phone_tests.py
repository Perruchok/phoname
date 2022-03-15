# Import the unittest library and our function
import unittest
from helpers import convert, symbol_relations, print_number 
from unittest.mock import patch 

# Test convert function 
class TestConvert(unittest.TestCase):

    MAPPING = {
        "(": "open_parenthesis",
        ")": "close_parenthesis",
        "-": "minus", 
        " ": "space",
        "+": "+",
        "0": "0", 
        "1": "1", 
        "2": "2",
        "3": "3", 
        "4": "4",
        "5": "5",
        "6": "6",
        "7": "7",
        "8": "8",
        "9": "9",
    }

    def _get_expected_output(self,number):

        return [
            f"{TestConvert.MAPPING[symbol]}.txt" for symbol in number
            ]

    def test_convert(self):

        expected_output = self._get_expected_output('( 5 6 8 3 )   + - 9 5 6 8 ')
        self.assertTrue(convert("(Love) +-Y568") == expected_output)

class TestPrinting(unittest.TestCase): 

    def test_invalid_input(self):
        self.assertRaises(FileNotFoundError,print_number,"+(you) #568")

    #@patch('helpers.print_number')
    def test_printing(self):

        expected_print = "".join(
        "     ___         ____________     __________      \n"
        "    |   |        |  _________|    |  _____   \    \n"
        "____|   |____    |  |             |_/    /  /     \n"
        "|            |   |  |______             /  /      \n"
        "|___     ____|   |________  \          /  /       \n"
        "    |   |                |   |        /  /        \n"
        "    |___|        ________|   /       /  \______   \n"
        "                 |_________ /       /__________|  \n"
        )

        list_to_print = ["+.txt", "space.txt", "5.txt", "space.txt", "2.txt", "space.txt"]

        line_to_print = print_number(list_to_print)

        self.assertEqual(expected_print, line_to_print)


# Run each of the testing functions
if __name__ == "__main__":
    unittest.main()