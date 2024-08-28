"""Gets the number of increases from a text file."""


def read_input(filename: str) -> list[str]:
    """Reads the file as a list"""
    with open(filename, "r", encoding="UTF-8") as f:
        return f.readlines()


def count_increases(data) -> int:
    """Counts the number of times the next number increases."""
    count = 0
    for i, depth in enumerate(data):
        if depth > data[i-1] and i != 0:
            count += 1
    return count


def three_sliding(data) -> list[int]:
    """Creates a list of 3 sliding window sums."""
    result = []
    final_index = len(data) - 3
    for i, num in enumerate(data):
        if i <= final_index:
            total = num + data[i+1] + data[i+2]
            result.append(total)
    return result


if __name__ == "__main__":
    file_data = read_input('data.txt')
    int_data = []
    for row in file_data:
        int_data.append(int(row))
    print(count_increases(int_data))
    print(count_increases(three_sliding(int_data)))
