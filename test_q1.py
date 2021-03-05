import unittest
import q1

class fizzTest(unittest.TestCase):
    def test_fizz(capfd):
        count()
        out, err = capfd.readouterr()
        assert out == "fizz"

    

if __name__ == "__main__":
    unittest.main(verbosity = 2)
