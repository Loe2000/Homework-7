import unittest
import fizzBuzz

class testCaseFizzBuzz(unittest.TestCase):
    def testFizz(self):
        self.assertEqual (fizzBuzz.fizzBuzz(9), "Fizz")
    


if __name__ == "__main__":
    unittest.main()