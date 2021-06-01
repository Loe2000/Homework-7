import unittest
import leapYear

class testCaseLeapYear(unittest.TestCase):
    def testmod400(self):
        self.assertEqual (leapYear.leapYear(2000), True)
    
    

if __name__ == "__main__":
    unittest.main()