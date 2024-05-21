"""
Vytvorte funkce encrypt a decrypt pro Caesarovu sifru.
Kompletni zadani v elearningu.
"""

def increase_letter(letter, offset):
    """
    Šifrování malých písmen
    """
    for _ in range(offset):
        if (ord(letter) + 1) > 122:
            letter = "a"
        else:
            letter = chr(ord(letter) + 1)
    return letter

def increase_big_letter(letter, offset):
    """
    Šifrování velkých písmen
    """
    for _ in range(offset):
        if (ord(letter) + 1) > 90:
            letter = "A"
        else:
            letter = chr(ord(letter) + 1)
    return letter

def decrease_letter(letter, offset):
    """
    Dešifrování malých písmen
    """
    for _ in range(offset):
        if (ord(letter) - 1) < 97:
            letter = "z"
        else:
            letter = chr(ord(letter) - 1)
    return letter

def decrease_big_letter(letter, offset):
    """
    Dešifrování velkých písmen
    """
    for _ in range(offset):
        if (ord(letter) - 1) < 65:
            letter = "Z"
        else:
            letter = chr(ord(letter) - 1)
    return letter

def encrypt(word, offset):
    """
    :param word - slovo k zasifrovani
    :param offset - znakovy posun
    :return: zasifrovane slovo
    """
    result = ""
    for letter in word:
        if letter.isalpha():
            if ord(letter) < 97:
                # změna pro velká písmena
                result += increase_big_letter(letter, offset)
            else:
                # změna pro malá písmena
                result += increase_letter(letter, offset)
        else:
            result += letter
    return result

def decrypt(word, offset):
    """
    :param word - zasifrovane slovo
    :param offset - znakovy posun
    :return: desifrovane slovo
    """
    result = ""
    for letter in word:
        if letter.isalpha():
            if ord(letter) < 97:
                # změna pro velká písmena
                result += decrease_big_letter(letter, offset)
            else:
                # změna pro malá písmena
                result += decrease_letter(letter, offset)
        else:
            result += letter
    return result

def main():
    """
    Hlavní funkce
    """
    encrypted = encrypt("PoCeM, tY BoBRe (jeDen) [moCalnIk]", 11)
    print(encrypted)
    decrypted = decrypt(encrypted, 11)
    print(decrypted)

if __name__ == "__main__":
    main()
