# Import the unittest library and our function
import unittest
from helpers import convert

# A class containing all of our tests
class Tests(unittest.TestCase):

    def test_1(self):
        self.assertTrue(convert("((Love)) + -You") == "aa5683bbd+dc968")      

# Run each of the testing functions
if __name__ == "__main__":
    unittest.main()