#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 12 20:13:34 2023

@author: ufabc
"""

#vezes_receita(pao, despensa)
def vezes_receita(receita, despensa):
    nomes_ingredientes = list(receita)
    ingrediente1 = nomes_ingredientes[0]    
    ingrediente2 = nomes_ingredientes[1]    
    ingrediente3 = nomes_ingredientes[2]
    n_ingrediente1 = despensa[ingrediente1] // receita[ingrediente1]    
    n_ingrediente2 = despensa[ingrediente2] // receita[ingrediente2]    
    n_ingrediente3 = despensa[ingrediente3] // receita[ingrediente3]   
    return(min(n_ingrediente1, n_ingrediente2, n_ingrediente3))     

def main():
    pao = {'farinha':50, 'fermento': 5, 'oleo': 10}
    
#    manteiga_igd = ('xerem', 'oleo')
#    manteiga_qtd = (100, 50)
    bolo = {'farinha': 100, 'acucar': 50, 'fermento': 10}

    #{'farinha': 500, 'fermento': 20, 'acucar': 0, 'oleo': 500}
    despensa = {'farinha':500, 'fermento': 20, 'oleo': 500, 'acucar': 0}    
    
    print(f'é possível fazer {vezes_receita(pao, despensa)} pães')
main()