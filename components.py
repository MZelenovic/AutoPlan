# -*- coding: utf-8 -*-
"""
Created on Wed Aug  2 11:19:53 2023
COMPONENTS
@author: Mladen Zelenovic
"""
import pandas as pd

from Capi_inicijal import planned_df
# import data
data = 'C:/Users/HP Probook 470/Desktop/Production_planing_Bosnia.xlsx'
components = pd.read_excel(data)
# omitting the first three lines
components.drop(index=[0, 1, 2], inplace=True)
# leaving only the required columns
components = components.loc[:, ['Unnamed: 1', 'Unnamed: 2', 'Unnamed: 6', 'Unnamed: 7']]
# renaming columns
components = components.rename(columns={'Unnamed: 1': 'ID', 'Unnamed: 2':'M_number', 'Unnamed: 6': 'component', 'Unnamed: 7': 'component_stock'})
# filling nan values
components['ID'] = components['ID'].fillna(method='ffill')
components['M_number'] = components['M_number'].fillna(method='ffill')
# droping duplicates
components.drop_duplicates(inplace=True)
# droping nan values
components.dropna(inplace=True)
#merging componennts with planned_df on ID
components = pd.merge(components, planned_df, on='ID', how='left')
components['component_stock'] = components['component_stock'].astype(float)
# subtracting planned values from componennts
components['component_stock'] -= components['Planirano'].fillna(0)
# droping column 'Planirano' and 'M_number' from updated components
components.drop(columns=['Planirano', 'M_number'], inplace=True)
# merging components with planned values on 'component'
planned_df.rename(columns={'ID':'component'}, inplace=True)
updated_components = pd.merge(components, planned_df, on='component', how='left')
# updating componennts with planned values
updated_components['component_stock'] += updated_components['Planirano'].fillna(0)
# grouping by 'ID' and transforming components into dictionary
updated_components = updated_components.groupby('ID').apply(lambda x: pd.Series({'components': dict(zip(x['component'], x['component_stock']))})).reset_index()
# Adding a 'Capacity' column that contains the minimum values ​​in the dictionaries
updated_components['Capacity'] = updated_components['components'].apply(lambda x: int(min(x.values())))

