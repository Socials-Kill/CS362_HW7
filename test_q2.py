import unittest
import q2

class yearTest(unittest.TestCase):
    def test_four(self):
        self.assertEqual(q2.leapYear(4), "This is a leap year.")
    
if __name__ == "__main__":
    unittest.main(verbosity = 2)
