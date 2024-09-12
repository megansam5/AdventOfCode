from main import find_next_button, button_from_coords, coords_from_button, find_code, list_to_int


def test_find_next_button():
    res = find_next_button(5, 'ULL')
    assert res == 1


def test_find_next_button2():
    res = find_next_button(1, 'RRDDD')
    assert res == 9


def test_find_next_button3():
    res = find_next_button(9, 'LURDL')
    assert res == 8


def test_find_next_button4():
    res = find_next_button(8, 'UUUUD')
    assert res == 5


def test_button_from_coods():
    res = button_from_coords((1, 1))
    assert res == 7


def test_button_from_coods2():
    res = button_from_coords((2, 3))
    assert res == 2


def test_button_from_coods3():
    res = button_from_coords((3, 2))
    assert res == 6


def test_coords_from_button():
    res = coords_from_button(7)
    assert res == (1, 1)


def test_coords_from_button2():
    res = coords_from_button(3)
    assert res == (3, 3)


def test_coords_from_button2():
    res = coords_from_button(2)
    assert res == (2, 3)


def test_find_code():
    data = ['ULL',
            'RRDDD',
            'LURDL',
            'UUUUD']
    res = find_code(data)
    assert res == [1, 9, 8, 5]


def test_list_to_int():
    res = list_to_int([1, 9, 8, 5])
    assert res == 1985
