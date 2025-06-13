import pytest
from Menu import Menu


class TestMenu:
    @pytest.fixture

    def menu(self):
        return Menu()

    def test_get_user_choice_valid(self, menu, monkeypatch):
        monkeypatch.setattr('builtins.input', lambda _: '2') 
        assert menu.get_user_choice() == 2

    def test_get_user_choice_out_range(self, menu, monkeypatch):
        monkeypatch.setattr('builtins.input', lambda _: '4')
        assert menu.get_user_choice() == -1

    
