from main import split_string_to_length, find_surface_area, find_ribbon_length


def test_split_string_to_length_valid():
    res = split_string_to_length('2x3x4')
    assert res == [2, 3, 4]


def test_split_string_to_length_valid2():
    res = split_string_to_length('1x1x10')
    assert res == [1, 1, 10]


def test_find_surface_area():
    res = find_surface_area([2, 3, 4])
    assert res == 58


def test_find_surface_area2():
    res = find_surface_area([1, 1, 10])
    assert res == 43


def test_find_ribbon_length():
    res = find_ribbon_length([2, 3, 4])
    assert res == 34


def test_find_ribbon_length2():
    res = find_ribbon_length([1, 1, 10])
    assert res == 14
