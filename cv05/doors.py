"""
Úkol 5.
Napište program, který načte soubor large.txt a pro každé dveře vyhodnotí,
zda je možné je otevřít nebo ne. Tedy vyhodnotí, zda lze danou množinu uspořádat
požadovaným způsobem. Výstup z programu uložte do souboru vysledky.txt ve
formátu 1 výsledek =  1 řádek. Na řádek napište vždy počet slov v množině a True
nebo False, podle toho, zda řešení existuje nebo neexistuje.

Podrobnější zadání včetně příkladu je jako obvykle na elearning.tul.cz
"""

from collections import defaultdict

def can_be_ordered(words):
    """
    Vytvoří se graf z začátečních a konečných písmen daných slov, který se následně projde
    """
    graph = defaultdict(list)
    in_degree = defaultdict(int)
    out_degree = defaultdict(int)
    num_of_notmatches = 0

    for word in words:
        first_letter = word[0]
        last_letter = word[-1]
        graph[first_letter].append(last_letter)
        out_degree[first_letter] += 1
        in_degree[last_letter] += 1

    for letter in graph:
        for _ in range(len(graph[letter])):
            if abs(in_degree[letter] - out_degree[letter]) > 1:
                num_of_notmatches += 1
        if num_of_notmatches < 2:
            pass
        else:
            return False
    return True

def read_and_solve(filename):
    """
    Načte soubor a zavolá funkci can_be_orderer pro pro každé načtené dveře
    """
    with open(filename, 'r',  encoding="UTF-8") as file:
        num_tests = int(file.readline())
        results = []

        for _ in range(num_tests):
            num_words = int(file.readline())
            words = [file.readline().strip() for _ in range(num_words)]
            results.append((num_words, can_be_ordered(words)))

        return results

def write_results(results, filename):
    """
    zapíše výsledek do souboru
    """
    with open(filename, 'w', encoding="UTF-8") as file:
        for num_words, result in results:
            file.write(f"{num_words} {result}\n")

def main():
    """
    Main function
    """
    #results = read_and_solve('./cv05/small.txt')
    results = read_and_solve('large.txt')
    write_results(results, 'vysledky.txt')

if __name__ == '__main__':
    main()
