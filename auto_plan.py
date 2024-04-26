# -*- coding: utf-8 -*-
"""
Created on Wed May 10 12:47:40 2023

@author: Mladen Zelenovic
"""

import pandas as pd
from radna_tabela import radna_tabela
from funkcije import filtriranje_norme

plan = radna_tabela.loc[:, ['M Number', 'ID', 'People qnt', 'Stvarna_norma', 'h.', 'Radno_mjesto']]
# DISPOSAL OF PRODUCTS THAT ARE NOT MANUFACTURED
plan = plan[plan['M Number'].str.startswith(('M', 'A'))]
# REJECTING PRODUCTS THAT HAVE NO CAPACITY FOR ONE BOX
plan = plan[plan['Stvarna_norma'] != 'Nema dovoljno ni za jednu kutiju']
# REJECTING PRODUCTS THAT DO NOT HAVE A SPECIFIC NUMBER OF WORKERS
plan = plan[plan['People qnt'] != 0]
# FILTERING OF WORKPLACES
plan = plan[plan['Radno_mjesto'] != 'Ne radi se']
# MAKING A PLAN FOR XX NUMBER OF PEOPLE
auto_plan = plan[plan['People qnt'].cumsum() <= 50]
print(auto_plan['People qnt'].sum())
# RESET INDEX
auto_plan = auto_plan.reset_index(drop=True)
# RENAME COLUMNS
auto_plan = auto_plan.rename(columns={'M Number' : 'M_broj','ID' :'Sifra', 'People qnt' : 'Broj_ljudi'})
# NORM FILTERING
auto_plan['Stvarna_norma'] = auto_plan.apply(lambda row: filtriranje_norme(row['Sifra'], row['Stvarna_norma']), axis=1)
# EXTRACTING THE EXCEL TABLE
auto_plan.to_excel('C:/Users/HP Probook 470/Desktop/Capi/auto_plan.xlsx', index=True)
