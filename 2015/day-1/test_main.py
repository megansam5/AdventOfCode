from main import calculate_floor, create_one_string, which_position_to_basement


def test_calculate_floor_valid():
    res = calculate_floor('(())')
    assert res == 0


def test_calculate_floor_valid2():
    res = calculate_floor('(()(()(')
    assert res == 3


def test_calculate_floor_valid3():
    res = calculate_floor('))(((((')
    assert res == 3


def test_calculate_floor_valid4():
    res = calculate_floor('))(')
    assert res == -1


def test_calculate_floor_valid5():
    res = calculate_floor(')())())')
    assert res == -3


def test_calculate_floor_valid():
    res = calculate_floor(')))')
    assert res == -3


def test_create_one_string():
    data = ['))', '(()', '()']
    res = create_one_string(data)
    assert res == '))(()()'


def test_which_position_to_basement():
    res = which_position_to_basement(')')
    assert res == 1


def test_which_position_to_basement2():
    res = which_position_to_basement('()())')
    assert res == 5
