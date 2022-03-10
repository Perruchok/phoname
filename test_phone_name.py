# Import the unittest library and our function
import unittest
from helpers import convert, print_number
from mock import patch


# Test convert function.
class TestsConvert(unittest.TestCase):
    MAPPER = {
        "+": "plus",
        "-": "dash",
        "(": "close-parenthesis",
        ")": "open-parenthesis",
    }

    def _get_expected_output(number):
        return [
            f"{MAPPER['symbol']}.txt" for symbol in number
        ]

    def test_letters_to_number(self):
        expected_output = self._get_expected_output("+52 (568) 123-74239")
        self.assertTrue(convert("+52 (love) 1cf-pg2bvz") == expected_output)

    def test_it_does_not_convert_numbers(self):
        expected_output = self._get_expected_output("+52 (568) 123-74239")
        self.assertTrue(convert("+52 (568) 123-74239") == expected_output)


# TODO: do this test.
class TestsConvert(unittest.TestCase):



class MyTest(TestCase):

    @patch('print')
    def test_letters_to_number(self, mock_print):
        # TODO: Learn how a function is mock.
        # You will have to mock the "print" function.
        # Resources: https://docs.python.org/3/library/unittest.mock.html

        expected_line_to_print = "\n".join([
            "  / _   |     |  _____   \ ",
            " / / |  |     |_/    /  /  ",
            " / / |  |     |_/    /  /  ",
        ])

        print_number([
            "1.txt", 
            "2.txt",
        ])

        line_to_print, kwargs = mock_print.call_args 
        self.assertEqual(line_to_print, expected_line_to_print)






# Run each of the testing functions
if __name__ == "__main__":
    unittest.main()