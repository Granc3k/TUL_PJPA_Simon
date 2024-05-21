# -*- coding: utf-8 -*-

"""
Cvičení 8. - karetní game poker

Vaším dnešním úkolem je zpracovat soubor se záznamy her a vyhodnotit,
kolikrát vyhrál druhý hráč.

Kompletní zadání je jako vždy na https://elearning.tul.cz/

"""
import gzip

# enums
LIST_OF_COLORS = ["H", "C", "D", "S"]
LIST_OF_NUMBERS = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]


class Game:
    """
    Třída reprezentující jednu hru pokeru
    """

    def __init__(self, line: str):
        parsed_line = line.split(" ")
        self.player1 = parsed_line[0:5]
        self.player2 = parsed_line[5:10]

    def card_ranks(self, hand):
        "Vrátí seznam hodnot karet, seřazený s nejvyšší hodnotou na prvním místě."
        ranks = ["--23456789TJQKA".index(r[0]) for r in hand]
        ranks.sort(reverse=True)
        return ranks

    def is_flush(self, hand):
        "Vrátí True, pokud mají všechny karty stejnou barvu."
        suits = [s[1] for s in hand]
        return len(set(suits)) == 1

    def is_flush_return(self, hand):
        "Vrátí nejvyšší kartu v ruce, pokud mají všechny karty stejnou barvu."
        if self.is_flush(hand):
            return self.max_card(hand)
        return False

    def is_straight(self, hand):
        "Vrátí True, pokud tvoří seřazené hodnoty postupku."
        ranks = self.card_ranks(hand)
        return (max(ranks) - min(ranks) == 4) and len(set(ranks)) == 5

    def is_straight_return(self, hand):
        "Vrátí nejvyšší kartu postupky."
        if self.is_straight(hand):
            return self.max_card(hand)
        return False

    def max_card(self, hand):
        "Vrátí nejvyšší kartu v ruce."
        ranks = self.card_ranks(hand)
        return ranks[0]

    def is_kind(self, n, hand):
        "Vrátí True, pokud jsou v ruce n karty se stejnou hodnotou."
        ranks = self.card_ranks(hand)
        for r in ranks:
            if ranks.count(r) == n:
                return True
        return False

    def is_kind_return(self, n, hand):
        "Vrátí hodnotu karty, pokud jsou v ruce n karty se stejnou hodnotou."
        ranks = self.card_ranks(hand)
        for r in ranks:
            if ranks.count(r) == n:
                return r
        return False

    def is_two_pair(self, hand):
        "Vrátí True, pokud jsou v ruce dvě páry."
        pair1 = self.is_kind_return(2, hand)
        if pair1:
            hand = [r for r in hand if r[0] != "--23456789TJQKA"[pair1]]
            pair2 = self.is_kind_return(2, hand)
            if pair2 and pair2 != pair1:
                if pair1 > pair2:
                    return pair2, pair1
                return pair1, pair2
        return False

    def is_full_house(self, hand):
        "Vrátí True, pokud je v ruce trojice a pár."
        if self.is_kind(3, hand) and self.is_kind(2, hand):
            return self.is_kind_return(3, hand), self.is_kind_return(2, hand)
        return False

    def is_four_of_a_kind(self, hand):
        "Vrátí True, pokud jsou v ruce čtyři karty se stejnou hodnotou."
        return self.is_kind_return(4, hand)

    def is_straight_flush(self, hand):
        "Vrátí True, pokud je ruka postupka ve stejné barvě."
        return self.is_straight(hand) and self.is_flush(hand)

    def is_straight_flush_return(self, hand):
        "Vrátí nejvyšší kartu postupky ve stejné barvě."
        if self.is_straight_flush(hand):
            return self.max_card(hand)
        return False

    def is_royal_flush(self, hand):
        "Vrátí True, pokud je ruka královská postupka."
        ranks = self.card_ranks(hand)
        return self.is_straight_flush(hand) and (max(ranks) == 14)

    def is_one_pair(self, hand):
        "Vrátí True, pokud je v ruce pár."
        return self.is_kind_return(2, hand)

    def is_three_of_a_kind(self, hand):
        "Vrátí True, pokud je v ruce trojice."
        return self.is_kind_return(3, hand)


def load_data(filename: str) -> list:
    """
    Načte data ze souboru a vrátí je jako list
    :param filename: jméno souboru
    :return: list her
    """
    with gzip.open(filename, "rt") as f:
        obsah = f.readlines()
    return obsah


def process_data(game: Game) -> int:
    """
    Zpracuje data z jedné hry a vrátí, zda vyhrál druhý hráč
    :param game: instance hry
    :return: 1 pokud vyhrál druhý hráč, jinak 0
    """
    # Hodnocení deku pro hráče 1
    player1_rank = (
        game.is_royal_flush(game.player1),
        game.is_straight_flush_return(game.player1),
        game.is_four_of_a_kind(game.player1),
        game.is_full_house(game.player1),
        game.is_flush_return(game.player1),
        game.is_straight_return(game.player1),
        game.is_three_of_a_kind(game.player1),
        game.is_two_pair(game.player1),
        game.is_one_pair(game.player1),
        game.card_ranks(game.player1),
    )

    # Hodnocení deku pro hráče 2
    player2_rank = (
        game.is_royal_flush(game.player2),
        game.is_straight_flush_return(game.player2),
        game.is_four_of_a_kind(game.player2),
        game.is_full_house(game.player2),
        game.is_flush_return(game.player2),
        game.is_straight_return(game.player2),
        game.is_three_of_a_kind(game.player2),
        game.is_two_pair(game.player2),
        game.is_one_pair(game.player2),
        game.card_ranks(game.player2),
    )

    # Porovnání hodnocení rukou hráčů
    for i in range(len(player1_rank)):
        if player1_rank[i] != player2_rank[i]:
            if player1_rank[i] and not player2_rank[i]:
                return 0
            if not player1_rank[i] and player2_rank[i]:
                return 1
            if player1_rank[i] > player2_rank[i]:
                return 0
            return 1


def validate_line(line: str) -> bool:
    """
    Zkontroluje zda, karty zadané na řádku jsou validní
    """
    splited_line = line.split(" ")
    for card in splited_line:
        if (card[0] not in LIST_OF_NUMBERS) or (card[1] not in LIST_OF_COLORS):
            return False
    return True


def main(filename: str) -> int:
    """
    filename - jméno souboru ke zpracování
    :return - počet vítězných her druhého hráče
    """
    player_2_wins = 0
    data = load_data(filename)
    for line in data:
        line = line.replace("\n", "")
        if validate_line(line):
            game = Game(line)
            player_2_wins += process_data(game)
        else:
            print("Karty nebylo možné vytvořit")
    return player_2_wins


if __name__ == "__main__":
    RES = main("poker.txt.gz")
    print(f"druhý hráč vyhrál {RES} her")
