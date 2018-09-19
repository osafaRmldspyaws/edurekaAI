#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
Subject  :  Function to calculate entropy of a given dataset
Author   :  Osafa Karim [osafa.karim@gmail.com]
Date     :  18/09/2018

"""
import sys
import math
from collections import Counter

def entropy_cal(dataset):
    
    ent_list =[]

    for col_name in dataset.columns:
        print(col_name)
        dic, tot = Counter(dataset[col_name]), float(len(dataset[col_name]))
        ent = -sum( count/tot * math.log(count/tot, 2) for count in dic.values())
        ent_list.append(ent)
        
    return ent_list

#sys.stderr.write(entropy_cal(dataset=))