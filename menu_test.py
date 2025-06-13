#################################################################################
#   Program Name: Dice Checker
#
#   Author: Lex Albrandt
#
#   Date: 06/13/25
#
#   File Name: menu_test.py
#
#   Version: 1.0
#
#   File purpose: Glass box testing for all menu functions
#################################################################################
import pytest
from Menu import Menu
from unittest.mock import Mock
from Compute import Compute


class TestMenu:
    @pytest.fixture
    # This creates a mock object of compute for testing purposes
    def mock_compute(self):
        return Mock(spec=Compute)

    @pytest.fixture
    def menu(self, mock_compute):
        return Menu(mock_compute)
    
    def test_menu_initialization(self, menu):
        assert menu._user_choice == 0
        assert menu._quit_choice == ''
        assert isinstance(menu._compute, Mock)

    def test_get_user_choice_valid_not_quit(self, menu, monkeypatch, capsys):
        inputs = iter(['5', '2'])
        monkeypatch.setattr('builtins.input', lambda _: next(inputs)) 

        result1 = menu.get_user_choice()
        result2 = menu.get_user_choice()

        assert result1 == -1                # tests '5': out of range
        assert result2 == 2                 # tests '2': valid input

    def test_get_user_choice_quit_scenarios(self, menu, monkeypatch, capsys):
        # Test quit with 'y'
        inputs = iter(['3', 'y'])
        monkeypatch.setattr('builtins.input', lambda _: next(inputs))
        result = menu.get_user_choice()
        assert result == 3

        # Test quit with 'n'
        inputs = iter(['3', 'n'])
        monkeypatch.setattr('builtins.input', lambda _: next(inputs))
        result = menu.get_user_choice()
        assert result == 0

        # Test quit with invalid input
        inputs = iter(['3', 'x', 'y'])
        monkeypatch.setattr('builtins.input', lambda _: next(inputs))
        result = menu.get_user_choice()
        captured = capsys.readouterr()
        assert result == 3
        assert "Invalid input. Please enter 'y' or 'n'.\n" in captured
        assert result == 3

    

        
        

    
