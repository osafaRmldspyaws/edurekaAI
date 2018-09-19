# -*- coding: utf-8 -*-
"""
Subject  :  This file loads the geospatial data downloaded as zip file.
Author   :  Osafa Karim [osafa.karim@gmail.com]
Date     :  18/09/2018

"""
import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd
import os

#os.chdir('zip_file_path') # path where the zip file has been downloaded

from zipfile import ZipFile

file_list = ['./ne_110m_rivers_lake_centerlines.zip']

for archive in file_list:
    zfile = ZipFile(archive)
    zfile.extractall('./data/')
    
shp_file = './data/ne_110m_rivers_lake_centerlines.dbf'
river_data = gpd.read_file(shp_file)

#Perform few exploratory commands just to get a hang of how the data is

river_data.head()
river_data.info()
river_data.shape
river_data.plot()

#removing unnecessary features
river_df = river_data.iloc[:,:9]
river_df.shape