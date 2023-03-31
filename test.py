from file_management import *
from main import *


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


def test_level_2():
    result = "\n".join(level2("example"))
    test = read_example(2)
    assert result == test


def test_level_3x(file_id: str | int):
    rounds = level3(file_id)
    for result in rounds:
        # test = read_example(3)
        print(result)
        result = tournament_round(result)
        print(result)
        result = tournament_round(result)
        print(result)
        assert result.count("R") < 1
        assert result.count("S") > 0


def test_level_3():
    test_level_3x("example")
    for i in range(1, 6):
        test_level_3x(i)


def test_level_4x(file_id: str | int):
    rounds = level4(file_id)
    for result in rounds:
        print(result)
        while len(result) > 1:
            result = tournament_round(result)
            print(result)
        assert result == "S"


def test_level_4():
    test_level_4x("example")
    for i in range(1, 6):
        test_level_4x(i)


if __name__ == "__main__":
    #test_level_0()
    #test_level_1()
    #test_level_2()
    #test_level_3()
    test_level_4()
