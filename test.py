from read_input import read_input_lines, read_input_text


def process_level_0(lines: list[str]) -> int:
    return 0


def test_level_0():
    lines = read_input_lines(0, 0)
    result = process_level_0(lines)
    test = read_input_text(0, 0, "test")
    assert result == int(test)


if __name__ == '__main__':
    test_level_0()
