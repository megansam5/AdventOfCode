def read_input(filename: str) -> list[str]:
    with open(filename, "r") as f:
        return f.readlines()


def count_increases(data) -> int:
    count = 0
    for i, depth in enumerate(data):
        if depth > data[i-1] and i != 0:
            count += 1
    return count


if __name__ == "__main__":
    data = read_input('data.txt')
    int_data = []
    for row in data:
        int_data.append(int(row))
    print(count_increases(int_data))
