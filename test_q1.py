import unittest
import q1

class fizzTest(unittest.TestCase):
    def test_fizz(self):
        self.assertEqual(q1.count(), "fizz")
    
    def test_buzz(self):
        self.assertEqual(q1.count(), "buzz")

    def test_fizzbuzz(self):
        self.assertEqual(q1.count(), "fizzbuzz")

if __name__ == "__main__":
    unittest.main(verbosity = 2)
