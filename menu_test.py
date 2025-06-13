import pytest
from Menu import Menu


class TestMenu:
    @pytest.fixture

    def menu(self):
        return Menu()
    
    def test_menu_initialization(self, menu):
        assert menu.user_choice == 0
        assert menu.quit_choice == ''

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

        
        

    
