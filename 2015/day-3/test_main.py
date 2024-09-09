
from main import create_one_string, create_dict_of_coordinates, count_houses, create_dict_of_coords_with_robo


def test_create_one_string():
    data = ['^^', '>>', '<<']
    res = create_one_string(data)
    assert res == '^^>><<'


def test_create_dict_of_coords():
    res = create_dict_of_coordinates('>')
    assert res == {'0,0': 1, '1,0': 1}


def test_create_dict_of_coords2():
    res = create_dict_of_coordinates('^>v<')
    assert res == {'0,0': 2, '0,1': 1, '1,1': 1, '1,0': 1}


def test_create_dict_of_coords3():
    res = create_dict_of_coordinates('^v^v^v^v^v')
    assert res == {'0,0': 6, '0,1': 5}


def test_count_houses():
    res = count_houses({'0,0': 2, '0,1': 1, '1,1': 1, '1,0': 1})
    assert res == 4


def test_count_houses2():
    res = count_houses({'0,0': 1, '1,0': 1})
    assert res == 2


def test_count_houses3():
    res = count_houses({'0,0': 6, '0,1': 5})
    assert res == 2


def test_create_dict_of_coords_with_robo():
    res = create_dict_of_coords_with_robo('^v')
    assert res == {'0,0': 1, '0,1': 1, '0,-1': 1}


def test_create_dict_of_coords_with_robo2():
    res = create_dict_of_coords_with_robo('^>v<')
    assert res == {'0,0': 3, '0,1': 1, '1,0': 1}


def test_create_dict_of_coords_with_robo3():
    res = create_dict_of_coords_with_robo('^v^v^v^v^v')
    assert res == {'0,0': 1, '0,1': 1, '0,-1': 1, '0,2': 1, '0,-2': 1,
                   '0,3': 1, '0,-3': 1, '0,4': 1, '0,-4': 1, '0,5': 1, '0,-5': 1}
