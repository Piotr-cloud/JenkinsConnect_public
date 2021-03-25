'''
Created on Mar 24, 2021

@author: piotr
'''
import unittest

from sum_ import *

class TestSum(unittest.TestCase):


    def test_1_plus_2(self):
        result = sum_(1,2)
        
        self.assertEqual(result, 3, " 1 + 2 != 3 ")
       
   

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()