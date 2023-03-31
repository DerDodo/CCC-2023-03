from file_management import *


def level1(file_id: int | str):
    lines = read_input_lines(1, file_id)
    results = []
    for i in range(int(lines[0])):
        match "".join(sorted(lines[i + 1])):
            # PRS
            case "PP":
                results += "P"
            case "PR":
                results += "P"
            case "PS":
                results += "S"
            case "RR":
                results += "R"
            case "RS":
                results += "R"
            case "SS":
                results += "S"
            case _:
                raise ValueError

    print_result_file_lines(1, file_id, results)
    return results


if __name__ == "__main__":
    level1()
