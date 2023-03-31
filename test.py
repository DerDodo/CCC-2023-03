from file_management import *
from main import level1


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
    lines = read_input_lines(0, "example")
    result = process_level_0(lines)
    test = read_example(0)
    print_result_file_lines(0, "example", [str(result)])
    assert result == int(test)


def test_level_1():
    result = "\n".join(level1("example"))
    test = read_example(1)
    assert result == test


if __name__ == "__main__":
    test_level_0()
    test_level_1()
