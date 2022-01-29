import pytest
from . .models import Cheese
from .factories import CheeseFactory

pytestmark = pytest.mark.django_db

def test__str__():
    cheese = CheeseFactory(name="Stracchino")
    assert cheese.__str__() == "Stracchino"
    assert str(cheese) == "Stracchino"
