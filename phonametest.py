# Import the unittest library and our function
import unittest
from phoname import convert,dict,special

# A class containing all of our tests
class Tests(unittest.TestCase):

    def test_1(self):
        self.assertTrue(convert("+52love",dict,special) == "+525683")

    def test_2(self):
        self.assertTrue(convert("+5 eat - tacos",dict,special) == "+5d328dcd82267") 

    def test_3(self):
        self.assertTrue(convert("+ (273) 568-996",dict,special) == "+da273bd568c996")

    def test_4(self):
        self.assertTrue(convert("((Love)) + -You",dict,special) == "aa5683bbd+dc968")      



# Run each of the testing functions
if __name__ == "__main__":
    unittest.main()