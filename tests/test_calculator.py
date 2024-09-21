import pytest
from programs import calculator

def test_add():
    assert calculator.add(3,5)==8
    
