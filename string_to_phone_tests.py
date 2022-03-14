# Import the unittest library and our function
import unittest
from helpers import convert, symbol_relations

# Test convert function 
class TestConvert(unittest.TestCase):

    MAPPER = {
        "(": "open_parenthesis",
        ")": "close_parenthesis",
        "-": "minus", 
        " ": "space",
    }

    def _get_expected_output(self,number):
        return [
            f"" f"{TestConvert.MAPPER[symbol]}.txt" for symbol in number
            ]

    def test_convert(self):
        expected_output = self._get_expected_output('((5683)) + -968')
        self.assertTrue(convert("((Love)) + -You") == expected_output)

# Run each of the testing functions
if __name__ == "__main__":
    unittest.main()