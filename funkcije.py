# -*- coding: utf-8 -*-
"""
Created on Mon May  8 09:12:10 2023

@author: Mladen Zelenovic
"""

from stolovi import stolovi
import pandas as pd


# choosing a workplace
def radno_mjesto(zeljeni_proizvod):
    radni_sto = 'Ne radi se'
    for sto, lista_proizvoda in stolovi.items():
        for proizvod in lista_proizvoda:
            if proizvod == zeljeni_proizvod:
              radni_sto = sto
            
    return radni_sto

# determining the norm
def Stvarna_norma (norm, string,capacity):
    Norma = None
    if string == '-':
        Norma = norm
        return Norma
    pakovanje = int(string.rsplit('x')[-1].strip())
    if capacity < pakovanje:
        Norma = 'Nema dovoljno ni za jednu kutiju'
        return Norma
    if norm == 0:
        Norma = 'Norma nije određena'
        return Norma
    if capacity >= norm:
        if (norm % pakovanje) == 0:
            Norma = norm
        else:
            Norma = ((norm // pakovanje) + 1) * pakovanje
    else:
        Norma = capacity - (capacity % pakovanje)
    return Norma

# determining the number of working hours for a given norm
def sati(norma, planirana_norma):
    norma_za_sat = norma / 7.5
    if planirana_norma == 'Norma nije određena' or planirana_norma == 'Nema dovoljno ni za jednu kutiju':
        planirani_sati = ''
        return planirani_sati
    if float(planirana_norma) >= norma:
        planirani_sati = 7.5
    else:
        planirani_sati = round(float(planirana_norma) / norma_za_sat, 1)
    return planirani_sati

# norm filtering    
def filtriranje_norme(sifra, norma):
    if '+' in sifra:
        norma = 'kao gotov proizvod'
    else:
        norma = norma
    return norma

# removal of unnecessary tools from workplaces
def alati_za_spustanje(lista_proizvoda, stolovi):
    nepotrebni_alati = {}

    for sto in stolovi.keys():
        nepotrebni_proizvodi = []
    
        for proizvod in stolovi[sto]:
            if not any(proizvod.startswith(x) for x in lista_proizvoda):
                nepotrebni_proizvodi.append(proizvod)
    
        nepotrebni_alati[sto] = nepotrebni_proizvodi
    
    nepotrebni_alati = {k: v for k, v in nepotrebni_alati.items() if v}   
    new_dict= {'radno_mjesto': list(nepotrebni_alati.keys()), 'proizvodi': list(nepotrebni_alati.values())}
    tabela_nepotrebni_alati = pd.DataFrame(new_dict)
    tabela_nepotrebni_alati = tabela_nepotrebni_alati.dropna(subset=['proizvodi'])
    tabela_nepotrebni_alati.to_excel('C:/Users/HP Probook 470/Desktop/Capi/Alati_za_spustanje.xlsx', index=False)
    
    return tabela_nepotrebni_alati

# removal of autoplan columns
def del_auto_plan(planned, string):
    if string == 'Yes':
        planned = 0
    else:
        planned = planned
    return planned











    