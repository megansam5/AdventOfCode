"""Tests for day 3."""

from main import three_sides, check_valid_triangle


def test_three_sides():
    res = three_sides('5 10 25')
    assert res == [5, 10, 25]


def test_three_sides2():
    res = three_sides('5    10   25')
    assert res == [5, 10, 25]


def test_three_sides3():
    res = three_sides(' 91  422  981')
    assert res == [91, 422, 981]


def test_check_valid_triangle_invalid():
    res = check_valid_triangle([5, 10, 25])
    assert res == False


def test_check_valid_triangle_valid():
    res = check_valid_triangle([2, 3, 4])
    assert res == True


# 919  652  409

def test_check_valid_triangle_valid2():
    res = check_valid_triangle([919, 652, 409])
    assert res == True
