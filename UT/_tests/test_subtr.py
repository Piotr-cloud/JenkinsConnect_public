'''
Created on Mar 24, 2021

@author: piotr
'''

import unittest

from subtr import subtract

class TestSubtr(unittest.TestCase):


    def test_2_minus_1(self):
        result = subtract(2,1)
        
        self.assertEqual(result, 1, " 2 - 1  != 1 ")
        
