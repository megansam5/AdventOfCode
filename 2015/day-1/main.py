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


if __name__ == "__main__":
    data = open_data('data.txt')
    data = create_one_string(data)
    print(calculate_floor(data))
