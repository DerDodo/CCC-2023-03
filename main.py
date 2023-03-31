from file_management import *


def get_winner(text: str) -> str:
    match "".join(sorted(text)):
        # PRS
        case "PP":
            return "P"
        case "PR":
            return "P"
        case "PS":
            return "S"
        case "RR":
            return "R"
        case "RS":
            return "R"
        case "SS":
            return "S"
        case _:
            raise ValueError

def level1(file_id: int | str):
    lines = read_input_lines(1, file_id)
    results = []
    for i in range(int(lines[0])):
        results += get_winner(lines[i + 1])

    print_result_file_lines(1, file_id, results)
    return results


def tournament_round(text: str) -> str:
    result = ""
    for j in range(0, len(text), 2):
        result += get_winner(text[j:j + 2])
    return result


def level2(file_id: int | str) -> list[str]:
    lines = read_input_lines(2, file_id)
    results = []
    for i in range(1, len(lines)):
        line = lines[i]
        line = tournament_round(line)
        line = tournament_round(line)
        print(line)
        results.append(line)
    print_result_file_lines(2, file_id, results)
    return results


if __name__ == "__main__":
    for sub in range(1, 6):
        level2(sub)
