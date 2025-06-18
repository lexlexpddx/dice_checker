#################################################################################
#   Program Name: Dice Checker
#
#   Author: Lex Albrandt
#
#   Date: 06/13/25
#
#   File Name: die_test.py
#
#   Version: 1.0
#
#   File purpose: Glass box functionality testing for the die class
#################################################################################

import pytest
from die import die

class Testdie:
    @pytest.fixture
    def die(self):
        return die()
    

    def test_die_initialization(self, die):
        assert die._num_samples == 0
        assert die._num_sides == 0
        assert die._deg_free == 0
        assert die._valid_choice == False
        assert die._side_list == []


    def test_get_sides_valid(self, die, monkeypatch):
        monkeypatch.setattr('builtins.input', lambda _: 20)
        die.get_sides()
        assert die._num_sides == 20
        assert die._deg_free == 19
        assert die._num_samples == 380


    def test_get_sides_invalid(self, die, monkeypatch, capsys):
        inputs = iter(['-4', '0', '21', '6'])
        monkeypatch.setattr('builtins.input', lambda _: next(inputs))
        
        die.get_sides()
        captured = capsys.readouterr()

        assert "Invalid input. Number of sides cannot be less than 1 or greater than 20" in captured.out
        assert "Invalid input. Number of sides cannot be less than 1 or greater than 20" in captured.out
        assert "Invalid input. Number of sides cannot be less than 1 or greater than 20" in captured.out

        assert die._num_sides == 6

    
    def test_get_roll_entries_valid(self, die, monkeypatch):
        die._num_sides = 4
        inputs = iter(['2', '3', '4', '5'])
        monkeypatch.setattr('builtins.input', lambda _: next(inputs))

        die.get_roll_entries()

        assert die._side_list[1] == 2
        assert die._side_list[2] == 3
        assert die._side_list[3] == 4
        assert die._side_list[4] == 5

    def test_get_roll_entries_invalid(self, die, monkeypatch):
        die._num_sides = 4
        inputs = iter(['-2', '2', '3', '4', '5'])
        monkeypatch.setattr('builtins.input', lambda _: next(inputs))

        die.get_roll_entries()

        assert die._side_list[1] == 2
        assert die._side_list[2] == 3
        assert die._side_list[3] == 4
        assert die._side_list[4] == 5