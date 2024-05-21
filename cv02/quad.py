#!/bin/env python
# -*- coding: utf-8 -*-
"""
PJP - cvičení číslo 2
"""
def body_jsou_stejne(a:tuple, b:tuple, c:tuple, d:tuple):
    result = ((a[0]==b[0] and a[1]==b[1]) or (a[0]==c[0] and a[1]==c[1]) or (a[0]==d[0] and a[1]==d[1]) or (b[0]==c[0] and b[1]==c[1]) or (b[0]==d[0] and b[1]==d[1]) or (c[0]==d[0] and c[1]==d[1]))
    return result

def na_stejne_primce(a, b, c):
    """Vrátí True, pokud body a, b a c leží na stejné přímce."""
    det = a[0]*(b[1] - c[1]) + b[0]*(c[1] - a[1]) + c[0]*(a[1] - b[1])
    return det == 0


    """
    Druhým úkolem je vytvořit funkci, která ze čtyř zadaných bodů určí, 
    zda tvoří konvexní čtyřúhelník.
    
    Body na vstupu jsou zadávány jako tuple (x, y) kde x a y mohou být
    libovolná reálná čísla, tedy i záporná. Body mohou vytvořit čtyřúhelník,
    ale není to pravidlem.

    Je potřeba aby funkce hlídala i extrémní situace, jako například,
    že body čtyřúhelník vůbec nevytváří. 
    """
    
def diagonaly(c1, c2, c3, c4):
    def determinant(p1, p2, p3):
        x1, y1 = p1
        x2, y2 = p2
        x3, y3 = p3
        return (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)

    cp1 = determinant(c1, c2, c3)
    cp2 = determinant(c2, c3, c4)
    cp3 = determinant(c3, c4, c1)
    cp4 = determinant(c4, c1, c2)

    if (cp1 < 0 and cp2 < 0 and cp3 < 0 and cp4 < 0) or (cp1 > 0 and cp2 > 0 and cp3 > 0 and cp4 > 0):
        return True
    else:
        return False

def is_convex(a:tuple, b:tuple, c:tuple, d:tuple):
    if (body_jsou_stejne(a,b,c,d)):
        return False
    if(na_stejne_primce(a,b,c) or na_stejne_primce(b,c,d) or na_stejne_primce(c,d,a) or na_stejne_primce(d,a,b)):
        return False
    return diagonaly(a, b, c, d)




if __name__ == '__main__':
    if(is_convex((0.0, 0.0), (1.0, 0.0), (1.0, 1.0), (0.0, 1.0))):
        print("je konvexní")
    else:
        print("není konvexní")
