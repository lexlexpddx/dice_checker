#################################################################################
#   Program Name: Dice Checker
#
#   Author: Lex Albrandt
#
#   Date: 06/13/25
#
#   File Name: compute_test.py
#
#   Version: 1.0
#
#   File purpose: Glass box functionality testing for the Compute class
#################################################################################

import pytest
from Compute import Compute

class TestCompute:
    @pytest.fixture
    def compute(self):
        return Compute()


    def test_compute_initialization(self, compute):
        assert compute._num_sides == 0
        assert compute._num_samples == 0
        assert compute._deg_free == 0
        assert compute._expect_freq == 0
        assert compute._text_input == ''
        assert compute._int_input == 0
        assert compute._valid_choice == False


    def test_get_sides_valid(self, compute, monkeypatch):
        monkeypatch.setattr('builtins.input', lambda _: 20)
        compute.get_sides()
        assert compute._num_sides == 20
        assert compute._deg_free == 19
        assert compute._num_samples == 380


    def test_get_sides_invalid(self, compute, monkeypatch, capsys):
        inputs = iter(['-4', '0', '21', '6'])
        monkeypatch.setattr('builtins.input', lambda _: next(inputs))
        
        compute.get_sides()
        captured = capsys.readouterr()

        assert "Invalid input. Number of sides cannot be less than 1 or greater than 20" in captured.out
        assert "Invalid input. Number of sides cannot be less than 1 or greater than 20" in captured.out
        assert "Invalid input. Number of sides cannot be less than 1 or greater than 20" in captured.out

        assert compute._num_sides == 6

       
        