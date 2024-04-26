# -*- coding: utf-8 -*-
"""
Created on Wed Aug  2 14:24:54 2023

@author: HP Probook 470
"""
import pandas as pd
from components import updated_components
from Capi_inicijal import capi

capi_final = pd.merge(capi, updated_components, on='ID', how='left')