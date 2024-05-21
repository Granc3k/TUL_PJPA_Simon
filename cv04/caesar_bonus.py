"""
Modul pro šifrování a dešifrování textu pomocí Caesarovy šifry.
"""
import os
import caesar

SOURCE_FILE = "source.txt"
END_FILE = "result.txt"

def num_words_on_line(line):
    """
    Počet slov na řádku
    """
    return len(line.split())

def calc_offset(lines):
    """
    Výpočet posunu pro šifrování
    """
    num_words = [num_words_on_line(line) for line in lines]
    return int(sum(num_words) / len(num_words))

def main():
    """
    Hlavní funkce
    """
    # ověření existence zdrojového souboru
    if not os.path.isfile(SOURCE_FILE):
        print("Chyba: Zdrojový soubor nenalezen.")
        return

    with open(SOURCE_FILE, "r", encoding="UTF-8") as source:
        lines = source.readlines()

    offset = calc_offset(lines)

    encrypted_lines = [caesar.encrypt(line, offset) for line in lines]

    with open(END_FILE, "w", encoding="UTF-8") as end:
        end.writelines(encrypted_lines)

if __name__ == "__main__":
    main()
