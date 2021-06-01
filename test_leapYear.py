import unittest
import leapYear

class testCaseLeapYear(unittest.TestCase):
    def testmod400(self):
        self.assertEqual (leapYear.leapYear(2000), True)
    def testmod100(self):
        self.assertEqual (leapYear.leapYear(1900), False)
    def testmod4(self):
        self.assertEqual (leapYear.leapYear(1024), True)
    def testnotLeap(self):
        self.assertEqual (leapYear.leapYear(1121), False)

if __name__ == "__main__":
    unittest.main()