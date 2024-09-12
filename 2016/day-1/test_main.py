"""Tests for day 1."""

from main import create_one_string, create_list_of_instructions, find_new_coords, find_direction, find_distance, coords_visted_twice


def test_create_one_string():
    data = ['R3, R5,', 'L1,', 'L3']
    res = create_one_string(data)
    assert res == 'R3, R5,L1,L3'


def test_create_list_of_instructions():
    res = create_list_of_instructions('R3, R5,L1,L3, R5, L7')
    assert res == ['R3', 'R5', 'L1', 'L3', 'R5', 'L7']


def test_find_new_coords():
    res = find_new_coords(['R2', 'L3'])
    assert res == [2, 3]


def test_find_new_coords2():
    res = find_new_coords(['R2', 'R2', 'R2'])
    assert res == [0, -2]


def test_find_new_coords3():
    res = find_new_coords(['R5', 'L5', 'R5', 'R3'])
    assert res == [10, 2]


def test_find_direction():
    res = find_direction('N', 'R')
    assert res == 'E'


def test_find_direction2():
    res = find_direction('S', 'R')
    assert res == 'W'


def test_find_direction3():
    res = find_direction('E', 'L')
    assert res == 'N'


def test_find_direction4():
    res = find_direction('S', 'L')
    assert res == 'E'


def test_find_distance():
    res = find_distance([2, 3])
    assert res == 5


def test_find_distance2():
    res = find_distance([0, -2])
    assert res == 2


def test_find_distance2():
    res = find_distance([-14, 21])
    assert res == 35


def test_coords_visited_twice():
    res = coords_visted_twice(['R8', 'R4', 'R4', 'R8'])
    assert res == [4, 0]
