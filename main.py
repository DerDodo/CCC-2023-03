from file_management import *


def get_winner(text: str) -> str:
    match "".join(sorted(text)):
        # LPRSY
        case "LL":
            return "L"
        case "LP":
            return "L"
        case "LR":
            return "R"
        case "LS":
            return "S"
        case "LY":
            return "L"
        case "PP":
            return "P"
        case "PR":
            return "P"
        case "PS":
            return "S"
        case "PY":
            return "P"
        case "RR":
            return "R"
        case "RS":
            return "R"
        case "RY":
            return "Y"
        case "SS":
            return "S"
        case "SY":
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


def fix_game3(players: str) -> str:
    nums = players.split(" ")
    R, P, S = int(nums[0][:-1]), int(nums[1][:-1]), int(nums[2][:-1])

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
        results.append(fix_game3(lines[i]))

    print_result_file_lines(3, file_id, results)
    # print(results)
    return results


def get_num_rounds(num_players):
    num_rounds = 0
    while num_players > 1:
        num_players //= 2
        num_rounds += 1
    return num_rounds - 1


def make_PRRR_packets(p, r, full_packet, num_rocks_in_full_packet):
    result = ""
    while p > 0 and r >= num_rocks_in_full_packet:
        result += full_packet
        p -= 1
        r -= num_rocks_in_full_packet
    return result, p, r


def fix_game4(players: str) -> str:
    nums = players.split(" ")
    R, P, S = int(nums[0][:-1]), int(nums[1][:-1]), int(nums[2][:-1])
    num_players = R + P + S
    num_rounds = get_num_rounds(P + R + S)
    num_rocks_in_full_packet = (2**num_rounds) - 1
    full_packet = "P" + "R" * num_rocks_in_full_packet

    result = ""

    while R > 0 and num_rocks_in_full_packet > 0:
        result_append, P, R = make_PRRR_packets(
            P, R, full_packet, num_rocks_in_full_packet
        )
        result += result_append
        num_rocks_in_full_packet = (num_rocks_in_full_packet + 1) // 2 - 1
        new_packet_length = len(full_packet) // 2
        full_packet = full_packet[0:new_packet_length]

    result += "P" * P + "R" * R + "S" * S
    assert len(result) == num_players
    return result


def fix_game5(players: str) -> str:
    nums = players.split(" ")
    R, P, S, Y, L = (
        int(nums[0][:-1]),
        int(nums[1][:-1]),
        int(nums[2][:-1]),
        int(nums[3][:-1]),
        int(nums[4][:-1]),
    )

    num_players = R + P + S + Y + L
    num_rounds = get_num_rounds(num_players)
    result = ""

    result += "P" * P + "R" * R + "Y" * Y + "L" * L + "S" * S
    print(result)
    assert len(result) == num_players
    return result


def level4(file_id: int | str) -> list[str]:
    lines = read_input_lines(4, file_id)
    results = []
    for i in range(1, len(lines)):
        results.append(fix_game4(lines[i]))

    print_result_file_lines(4, file_id, results)
    return results


def level5(file_id: int | str) -> list[str]:
    lines = read_input_lines(5, file_id)
    results = []
    for i in range(5, len(lines)):
        results.append(fix_game5(lines[i]))

    print_result_file_lines(5, file_id, results)
    return results


if __name__ == "__main__":
    for sub in range(1, 6):
        level2(sub)
