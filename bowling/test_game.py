import unittest
from game import Game


def test_bowling_game():
    game = Game()

    for i in range(21):
        game.roll(0)

    assert game.score() == 0
