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
        result += get_winner(text[j : j + 2])
    return result


def level2(file_id: int | str) -> list[str]:
    lines = read_input_lines(2, file_id)
    results = []
    for i in range(1, len(lines)):
        line = lines[i]
        line = tournament_round(line)
        line = tournament_round(line)
        results.append(line)
    print_result_file_lines(2, file_id, results)
    return results


def fix_game(players: str) -> str:
    nums = players.split(" ")
    R, P, S = int(nums[0][0]), int(nums[1][0]), int(nums[2][0])

    result = ""

    while P > 0 and R >= 3:
        result += "PRRR"
        P -= 1
        R -= 3
    while P > 0 and R > 0:
        result += "P" + "R" * R
        P -= 1
        R = 0

    return result + "P" * P + "S" * S


def level3(file_id: int | str) -> list[str]:
    lines = read_input_lines(3, file_id)
    results = []
    for i in range(1, len(lines)):
        results.append(fix_game(lines[i]))

    print_result_file_lines(3, file_id, results)
    # print(results)
    return results


if __name__ == "__main__":
    for sub in range(1, 6):
        level2(sub)
