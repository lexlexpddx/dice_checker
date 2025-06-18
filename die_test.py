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
        assert die._expected_freq == 0
        assert die._chi_squared_value == 0
        assert die._observed_value == 0
        assert die._p_value == 0
        assert die._significance_level == 0.05


    def test_get_sides_valid(self, die, monkeypatch):
        monkeypatch.setattr('builtins.input', lambda _: 20)
        die.get_sides()
        assert die._num_sides == 20
        assert die._deg_free == 19
        assert die._num_samples == 380
        assert die._expected_freq == 19


    def test_get_sides_invalid(self, die, monkeypatch, capsys):
        inputs = iter(['-4', '0', '21', '6'])
        monkeypatch.setattr('builtins.input', lambda _: next(inputs))
        
        die.get_sides()
        captured = capsys.readouterr()

        assert "Invalid input. Number of sides cannot be less than 4 or greater than 20" in captured.out
        assert "Invalid input. Number of sides cannot be less than 4 or greater than 20" in captured.out
        assert "Invalid input. Number of sides cannot be less than 4 or greater than 20" in captured.out

        assert die._num_sides == 6

    
    def test_get_roll_entries_valid(self, die, monkeypatch, capsys):
        # Set up the die properly
        die._num_sides = 4
        die._num_samples = 14  # Sum of 2+3+4+5
        die._expected_freq = 3  # Not critical but good to set
        
        # Create a sequence of inputs that will satisfy both the side entry
        # and the validation loop (needs to reach num_samples)
        inputs = iter(['2', '3', '4', '5'])
        monkeypatch.setattr('builtins.input', lambda _: next(inputs))
        
        # Patch time.sleep and os.system to do nothing
        monkeypatch.setattr('time.sleep', lambda _: None)
        monkeypatch.setattr('os.system', lambda _: None)

        die.get_roll_entries()
        
        # Check the expected values were stored
        assert die._side_list[1] == 2
        assert die._side_list[2] == 3
        assert die._side_list[3] == 4
        assert die._side_list[4] == 5

    def test_get_roll_entries_invalid(self, die, monkeypatch, capsys):
        # Set up the die properly
        die._num_sides = 4
        die._num_samples = 14  # Sum of 2+3+4+5
        die._expected_freq = 3  # Not critical but good to set
        die._valid_choice = True  # Start with valid choice
        
        # Create inputs that include an invalid value (-2) followed by valid ones
        inputs = iter(['-2', '2', '3', '4', '5'])
        monkeypatch.setattr('builtins.input', lambda _: next(inputs))
        
        # Patch time.sleep and os.system to do nothing
        monkeypatch.setattr('time.sleep', lambda _: None)
        monkeypatch.setattr('os.system', lambda _: None)

        die.get_roll_entries()
        
        # Capture output to verify error message
        captured = capsys.readouterr()
        assert "Number of rolls cannot be less than 0" in captured.out
        
        # Check the expected values were stored
        assert die._side_list[1] == 2
        assert die._side_list[2] == 3
        assert die._side_list[3] == 4
        assert die._side_list[4] == 5