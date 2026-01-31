import pytest
from src import calculator
from src.calculator import fun1, fun2, fun3, fun4, fun5, fun6, fun7

def test_fun1():
    assert calculator.fun1(2, 3) == 5
    assert calculator.fun1(5,0) == 5
    assert calculator.fun1 (-1, 1) == 0
    assert calculator.fun1 (-1, -1) == -2


def test_fun2():
    assert calculator.fun2(2, 3) == -1
    assert calculator.fun2(5,0) == 5
    assert calculator.fun2 (-1, 1) == -2
    assert calculator.fun2 (-1, -1) == 0

def test_fun3():
    assert calculator.fun3(2, 3) == 6
    assert calculator.fun3(5,0) == 0
    assert calculator.fun3 (-1, 1) == -1
    
    assert calculator.fun3 (-1, -1) == 1

def test_fun4():
    assert calculator.fun4(2, 3, 5) == 25  # (2+3)*5 = 25
    assert calculator.fun4(1, 2, 3) == 9   # (1+2)*3 = 9
    assert calculator.fun4(5, 5, 2) == 20  # (5+5)*2 = 20

def test_fun5():
    assert fun5(10, 2) == 5.0
    assert fun5(20, 4) == 5.0
    assert fun5(9, 3) == 3.0

def test_fun5_zero_division():
    with pytest.raises(ZeroDivisionError):
        fun5(10, 0)

def test_fun6():
    assert fun6(2, 3) == 8
    assert fun6(5, 2) == 25
    assert fun6(10, 0) == 1

def test_fun7():
    assert fun7([1, 2, 3, 4, 5]) == 3.0
    assert fun7([10, 20, 30]) == 20.0
    assert fun7([5]) == 5.0

def test_fun7_empty_list():
    with pytest.raises(ValueError):
        fun7([])
