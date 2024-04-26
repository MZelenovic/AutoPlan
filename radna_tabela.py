# -*- coding: utf-8 -*-
"""
Created on Wed May 10 07:34:56 2023

@author: Mladen Zelenovic
"""
import pandas as pd
from capi_final import capi_final
import funkcije


radna_tabela = capi_final.loc[:, ['M Number','ID', 'Production space', 'Pakovanje', 'Operations', 'People qnt', 'Norm', 'Production capacity', 'Capacity', 'Client backlog', 'Ship. backlog (LL)', 'Storage Free/Block', 'Backlog', 'Order', '14 days', '30 days', 'Next shipment', 'Planirano']]
# SUBTRACTION OF ALREADY PLANNED QUANTITIES FROM THE CAPACITY
radna_tabela['Production capacity'] = radna_tabela['Production capacity'] - radna_tabela['Planirano']

# REMOVAL OF COLUMNS THAT HAVE NO PLANING CAPACITY
radna_tabela = radna_tabela[radna_tabela['Production capacity'] > 0]
# CONVERSION OF NORMS AND CAPACITY IN INT. VALUES
radna_tabela['Norm'] = radna_tabela['Norm'].astype('int64')
radna_tabela['Production capacity'] = radna_tabela['Production capacity'].astype('int64')

radna_tabela['Stvarna_norma'] = radna_tabela.apply(lambda row: funkcije.Stvarna_norma(row['Norm'], row['Pakovanje'], row['Production capacity']), axis=1)

radna_tabela['Radno_mjesto'] = radna_tabela.apply(lambda row: funkcije.radno_mjesto(row['M Number']), axis=1)

radna_tabela['h.'] = radna_tabela.apply(lambda row: funkcije.sati(row['Norm'], row['Stvarna_norma']), axis=1)

# SORT BY NEXT SHIPMENT
radna_tabela= radna_tabela.sort_values(by='Next shipment', ascending=True)
# EXPORTING CAPI AS EXCEL DOCUMENT
radna_tabela.to_excel('C:/Users/HP Probook 470/Desktop/Capi/radna_tabela.xlsx', index=False)