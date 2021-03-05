import unittest
import q2

class yearTest(unittest.TestCase):
    def test_four(self):
        self.assertEqual(q2.leapYear(4), "This is a leap year.")
    
    def test_hundred(self):
        self.assertEqual(q2.leapYear(100), "This is not a leap year.")

    def test_fourHundred(self):
        self.assertEqual(q2.leapYear(400), "This is a leap year.")

if __name__ == "__main__":
    unittest.main(verbosity = 2)
