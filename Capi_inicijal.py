# -*- coding: utf-8 -*-
"""
Created on Sat May  6 22:01:37 2023

@author: Mladen Zelenovic
"""

import pandas as pd
from funkcije import del_auto_plan
# Loading data into the program
data = 'C:/Users/HP Probook 470/Desktop/utorak.xlsx'
capi = pd.read_excel(data)
# Filtering of products made in hall 4
capi = capi[capi['Production space'] == 'H4']
# omitting the autoplan
capi['Planned quantity'] = capi.apply(lambda row: del_auto_plan(row['Planned quantity'], row['Auto-planning']), axis=1)
capi['Planned quantity.1'] = capi.apply(lambda row: del_auto_plan(row['Planned quantity.1'], row['Auto-planning.1']), axis=1)
capi['Planned quantity.2'] = capi.apply(lambda row: del_auto_plan(row['Planned quantity.2'], row['Auto-planning.2']), axis=1)
capi['Planned quantity.3'] = capi.apply(lambda row: del_auto_plan(row['Planned quantity.3'], row['Auto-planning.3']), axis=1)
# replacing the nan values with 0
capi.fillna(0, inplace=True)
# adding a new column with total planned quantities
capi['Planirano'] = capi['Planned quantity'] + capi['Planned quantity.1'] + capi['Planned quantity.2'] + capi['Planned quantity.3']
# omitting unnecessary columns
capi = capi.drop(columns=['Assembly parameters', 'Auto-planning', 'Auto-planning.1', 'Auto-planning.2', 'Auto-planning.3', 'Planned quantity', 'Planned quantity.1', 'Planned quantity.2', 'Planned quantity.3', 'Shift 1', 'Shift 2', 'Shift 1.1', 'Shift 2.1', 'Client ship. days', 'Part request'])
# Rename column
capi.rename(columns={'Name': 'ID'}, inplace=True)
# omitting products that do not have material for the full norm or that do not have a Backlog
capi = capi[(capi['Production capacity'] >= capi['Norm']) | ((capi['Backlog'] != 0) & (~capi['Backlog'].isna()))]
# sorting by Backlog
capi= capi.sort_values(by='Backlog', ascending=False)
# converting the M number column to a string
capi['M Number'] = capi['M Number'].astype(str)
# creating a list of products
products = capi['M Number'].reset_index(drop=True)
planned_df = capi[capi['Planirano'] != 0][['ID', 'Planirano']]

# exporting capi as excel document
capi.to_excel('C:/Users/HP Probook 470/Desktop/Capi/inicijal.xlsx', index=False)
