# Import the unittest library and our function
import unittest
from helpers import convert

# Test convert function 
class TestConvert(unittest.TestCase):

    def test_1(self):
        self.assertTrue(convert("((Love)) + -You") == "aa5683bbd+dc968")

# Run each of the testing functions
if __name__ == "__main__":
    unittest.main()