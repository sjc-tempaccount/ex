"""
Test temp fns
"""
import unittest
import temp

class TempTest(unittest.TestCase):
    """
    Tests for temperature conversion module
    """

    def setUp(self):
        print("Setting up")

    def tearDown(self):
        print("Tearing down")

    def test_zero(self):
        """
        Celsius 0 is Fahrenheit 32
        Fahrenheit 0 is Celsius -32
        """
        self.assertAlmostEqual(temp.ctof(0),32)

    def test_val(self):
        """

        Celsius 0 is Fahrenheit 32
        Fahrenheit 0 is Celsius -32
        """
        self.assertEqual(temp.ctof(-40),-40)        

if __name__=="__main__":
    unittest.main()
        


