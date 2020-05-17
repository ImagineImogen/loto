import pytest
from player import Check, Player
from game import Game, Play

def test_index_2d():
    assert Game().index_2d([[0,1], [2,3]], 2) == (1, 0)

def test_winner():
    assert Game().winner(["[40]", "[65]", "85"]) == 0

def test_finished():
    p1 = Player(9, 3).card_making()
    pl_1, pl_1_list = p1[0], p1[1]
    p2 = Player(9, 3).card_making()
    pl_2, pl_2_list = p2[0], p2[1]
    playing = Play(100, pl_1, pl_2, pl_1_list, pl_2_list)
    assert playing.finished(player_1_list, player_1) == 0

def test_check_card():
    assert Check().check_card([]) == []

def test_card():
    assert Player(9,3).card([[0], [3], [6]]) == '|___0___||___3___||___6___|'

def test_blank():
    assert Player(9,3).blank(2)  == '__' or 2

def test_display():
    assert Player(9,3).display(1, '__', 2) == '|_______|'
