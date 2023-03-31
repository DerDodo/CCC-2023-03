def read_input_lines(level: int, file_id: str | int) -> list[str]:
    with open(f"input/level-{level}/level{level}_{file_id}.in") as file:
        return file.readlines()


def read_input_text(level: int, file_id: str | int) -> str:
    with open(f"input/level-{level}/level{level}_{file_id}.in") as file:
        return file.read()


def read_example(level: int) -> str:
    with open(f"input/level-{level}/level{level}_example.out") as file:
        return file.read()

def print_result_lines(level: int, file_id: int, lines: list[str]):
    pass
