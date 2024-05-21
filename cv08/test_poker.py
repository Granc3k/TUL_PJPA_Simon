"""
Cvičení 8. - testy hra poker

Implenentujte testy dle zadání

Kompletní zadání je jako vždy na https://elearning.tul.cz/
"""

from poker import Game
import poker


def test_card_ranks():
    """Test for card ranks."""
    game = Game("2H 3D 5S 9C KD 2C 3H 4S 8C AH")
    assert game.card_ranks(game.player1) == [13, 9, 5, 3, 2]
    assert game.card_ranks(game.player2) == [14, 8, 4, 3, 2]


def test_is_flush():
    """Test for flush."""
    game = Game("2H 3H 5H 9H KH 2C 3H 4S 8C AH")
    assert game.is_flush(game.player1)
    assert not game.is_flush(game.player2)


def test_is_straight():
    """Test for straight."""
    game = Game("2H 3D 4S 5C 6D 9C 3H 4S 5C 6H")
    assert game.is_straight(game.player1)
    assert not game.is_straight(game.player2)


def test_validate_line_true():
    """Test for validate line true."""
    assert poker.validate_line("2H 3D 5S 9C KD 2C 3H 4S 8C AH")


def test_validate_line_false():
    """Test for validate line false."""
    assert not poker.validate_line("2H 3Q 5S 9C KD 2C 3H 4S 8C AH")


def test_is_kind():
    """Test for kind."""
    game = Game("2H 2D 2S 9C KD 2C 3H 4S 8C AH")
    assert game.is_kind(3, game.player1)
    assert not game.is_kind(2, game.player2)
    assert not game.is_kind(4, game.player1)
    assert not game.is_kind(3, game.player2)


def test_is_two_pair():
    """Test for two pair."""
    game = Game("2H 2D 4S 4C KD 2C 3H 4S 8C AH")
    assert game.is_two_pair(game.player1)
    assert not game.is_two_pair(game.player2)


def test_is_full_house():
    """Test for full house."""
    game = Game("2H 2D 2S 3C 3D 2C 3H 4S 8C AH")
    assert game.is_full_house(game.player1)
    assert not game.is_full_house(game.player2)


def test_is_four_of_a_kind():
    """Test for four of a kind."""
    game = Game("2H 2D 2S 2C KD 2C 3H 4S 8C AH")
    assert game.is_four_of_a_kind(game.player1)
    assert not game.is_four_of_a_kind(game.player2)


def test_is_straight_flush():
    """Test for straight flush."""
    game = Game("2H 3H 4H 5H 6H 2C 3H 4S 8C AH")
    assert game.is_straight_flush(game.player1)
    assert not game.is_straight_flush(game.player2)


def test_is_royal_flush():
    """Test for royal flush."""
    game = Game("TH JH QH KH AH 2C 3H 4S 8C AH")
    assert game.is_royal_flush(game.player1)
    assert not game.is_royal_flush(game.player2)


def test_is_one_pair():
    """Test for one pair."""
    game = Game("2H 2D 5S 9C KD 2C 3H 4S 8C AH")
    assert game.is_one_pair(game.player1)
    assert not game.is_one_pair(game.player2)


def test_is_three_of_a_kind():
    """Test for three of a kind."""
    game = Game("2H 2D 2S 9C KD 2C 3H 4S 8C AH")
    assert game.is_three_of_a_kind(game.player1)
    assert not game.is_three_of_a_kind(game.player2)

def validate():
    "Test for process data."
    game = Game("4S 2H 2C 4C 8S 5H KC 8C QC QD")
    assert poker.process_data(game) == 0
