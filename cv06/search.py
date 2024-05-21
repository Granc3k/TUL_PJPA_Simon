# -*- coding: utf-8 -*-

""" 
Úkol 6.
Vaším dnešním úkolem je vytvořit program, který o zadaném textu zjistí některé
údaje a vypíše je na standardní výstup. Hlavním smyslem cvičení je procvičit
si práci s regulárními výrazy, takže pro plný bodový zisk je nutné použít k
řešení právě tento nástroj.

Program musí pracovat s obecným textem, který bude zadaný v souboru. Jméno
souboru bude zadáno jako vstupní parametr funkce main, která by měla být
vstupním bodem programu. Samozřejmě, že funkce main by neměla řešit problém
kompletně a měli byste si vytvořit další pomocné funkce. Můžete předpokládat,
že soubor bude mít vždy kódování utf-8 a že bude psaný anglicky, tedy jen
pomocí ASCII písmen, bez české (či jiné) diakritiky. 

Konkrétně musí program zjistit a vypsat:

1. Počet slov, která obsahují nejméně dvě samohlásky (aeiou) za sebou. Například
slovo bear.

2. Počet slov, která obsahují alespoň tři samohlásky - například slovo atomic.

3. Počet slov, která mají šest a více znaků - například slovo terrible.

4. Počet řádků, které obsahují nějaké slovo dvakrát. 

Podrobnější zadání včetně příkladu je jako obvykle na elearning.tul.cz
"""
import os
import re

def main(file_name):
    """
    zpracuje soubor a vypíše počty slov splňujících podmínky
    """
    if not os.path.isfile(file_name):
        print("Chyba: Zdrojový soubor nenalezen.")
        return

    with open(file_name, "r", encoding="UTF-8") as source:
        text = source.read().lower()

    words = re.findall(r'\b\w+\b', text)
    unique_words = set(words)
    lines = text.split('\n')

    print(sum(1 for word in unique_words if re.search(r'[aeiyou]{2}', word)))
    print(sum(1 for word in unique_words if sum(1 for char in word if char in 'aeiou') >= 3))
    print(sum(1 for word in unique_words if len(word) >= 6))
    print(sum(1 for line in lines if any(re.findall(r'\b\w+\b', line).count(word) >= 2 for word in
    set(re.findall(r'\b\w+\b', line)))))

if __name__ == '__main__':
    main('simple.txt')
