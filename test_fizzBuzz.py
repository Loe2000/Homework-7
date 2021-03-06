import unittest
import fizzBuzz

class testCaseFizzBuzz(unittest.TestCase):
    def testFizz(self):
        self.assertEqual (fizzBuzz.fizzBuzz(9), "Fizz")
    def testBuzz(self):
        self.assertEqual (fizzBuzz.fizzBuzz(20), "Buzz")
    def testFizzBuzz(self):
        self.assertEqual (fizzBuzz.fizzBuzz(135), "FizzBuzz")
    def testNone(self):
        self.assertEqual (fizzBuzz.fizzBuzz(52), 52)


if __name__ == "__main__":
    unittest.main()