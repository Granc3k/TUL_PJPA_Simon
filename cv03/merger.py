"""
Na vstupu jsou dány 3 sekvence. Každá z nich obsahuje několik uspořádaných
dvojic uložených jako tuple (id, count).
Sekvence může tedy vypadat například takto: ((1, 3), (3, 4), (10, 2)).
První prvek sekvence je tedy tuple s hodnotami  id = 1 je count = 3 a tak dále.
Vaším úkolem je spojit tyto tři sekvence do jednoho slovníku. Ten bude výstupem z programu.

Položky slovníku budou v následujícím tvaru {id: [A, B, C]},
kde A, B a C jsou hodnoty pro příslušné ID v první, druhé a třetí sekvenci.

Ovšem pozor - neplatí, že každé id je obsaženo ve všech sekvencích.
Může být ve všech, ve dvou, nebo pouze v jedné.

Tady máte konkrétní příklad. Zadané sekvence mají následující podobu:

line_a = ((1, 3), (3, 4), (10, 2))
line_b = ((1, 2), (2, 4), (5, 2))
line_c = ((1, 5), (3, 2), (7, 3))

Transformací musí vzniknout následující slovník:

{1: [3, 2, 5],
 2: [0, 4, 0],
 3: [4, 0, 2],
 5: [0, 2, 0],
 7: [0, 0, 3],
10: [2, 0, 0]}
"""


def merge_tuples(line_a, line_b, line_c):
    """
    Args:
        line_a (tuple)
        line_b (tuple)
        line_c (tuple)
    Returns:
        dictionary
    """
    # Vytvoření slovníků pro každou ze sekvencí
    dict_a = dict(line_a)
    dict_b = dict(line_b)
    dict_c = dict(line_c)

    # Spojení všech klíčů do jednoho celku
    all_keys = set(list(dict_a.keys()) + list(dict_b.keys()) + list(dict_c.keys()))

    # Vytvoření slovníku
    result = {}
    for key in all_keys:
        a = dict_a.get(key, 0)
        b = dict_b.get(key, 0)
        c = dict_c.get(key, 0)
        result[key] = [a, b, c]

    return result


def simple_visual_test():
    """
    Print výsledku je sice primitivní metoda, ale jako základní test
    slouží programátorům odjakživa...
    """
    line_a = ((1, 3), (3, 4), (10, 2))
    line_b = ((1, 2), (2, 4), (5, 2))
    line_c = ((1, 5), (3, 2), (7, 3))
    print(merge_tuples(line_a, line_b, line_c))

if __name__ == "__main__":
    simple_visual_test()
