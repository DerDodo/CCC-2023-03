from read_input import read_input_lines, read_input_text


def process_level_0(lines: list[str]) -> int:
    min_val = 100000000
    min_i = 0
    for i in range(1, len(lines)):
        val = int(lines[i])
        if val < min_val:
            min_val = val
            min_i = i
    return min_i - 1


def test_level_0():
    lines = read_input_lines(0, 0)
    result = process_level_0(lines)
    test = read_input_text(0, 0, "test")
    assert result == int(test)


if __name__ == '__main__':
    test_level_0()
