"""Day 1 - Not Quite Lisp"""


def open_data(filename: str) -> list[str]:
    """Open the data from another file."""
    with open(filename, 'r', encoding="UTF-8") as f:
        return f.readlines()


def create_one_string(data_list: list[str]) -> str:
    """Creates one string from a list (from data.txt)."""
    return "".join(data_list)


def calculate_floor(brackets: str) -> int:
    """Calculates the floor number from the string."""

    negatives = brackets.count(")")
    positives = brackets.count("(")
    score = positives - negatives
    return score


def which_position_to_basement(brackets: str) -> int:
    """returns the position when he enters floor -1."""
    current = 0
    position = 0
    while current >= 0:
        if brackets[position] == ')':
            current -= 1
        else:
            current += 1
        position += 1
    return position


if __name__ == "__main__":
    data = open_data('data.txt')
    data = create_one_string(data)
    print(calculate_floor(data))
    print(which_position_to_basement(data))
