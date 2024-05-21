# -*- coding: utf8 -*-
"""
Zakladni sablona pro prvni cviceni
"""
#made by Martin Šimon

def triangle(a: int, b:int, c:int):
    """
    Funkce vrací True nebo False, podle toho zda strany a, b, c mohou tvořit
    pravoúhlý trojúhelník

    Pro jednoduchost můžete předpokládat, že strany a, b jsou odvěsny, c je přepona. 
    Tak jako je to ve známé matematické poučce. 
    """
    return a**2+b**2 == c**2
