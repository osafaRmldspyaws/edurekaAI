# -*- coding: utf-8 -*-
"""
Subject  :  This contains the unit test cases to test the entropy function
Author   :  Osafa Karim [osafa.karim@gmail.com]
Date     :  18/09/2018

"""

import unittest
import entropy
import pandas as pd
import numpy as np


class TestEntropy(unittest.TestCase):
    
    def test_string_data(self):
        test_data = pd.DataFrame(['a','a','a','a'],
                           columns=['A'])
        
        result = entropy.entropy_cal(test_data)
        self.assertEqual(np.abs(result),0)
        
    def test_geospatial_data(self):
        test_data = river_df
        
        result = entropy.entropy_cal(test_data)
        self.assertEqual(len(result),9)
        
if __name__=='__main__':
    unittest.main()