def read_input_lines(level: int, file_id: int, file_name: str = "level") -> list[str]:
    with open(f"input/level-{level}/{file_name}{level}_{file_id}.in") as file:
        return file.readlines()


def read_input_text(level: int, file_id: int, file_name: str = "level") -> str:
    with open(f"input/level-{level}/{file_name}{level}_{file_id}.in") as file:
        return file.read()
