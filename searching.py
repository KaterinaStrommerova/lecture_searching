from pathlib import Path
import json


def read_data(file_name, field):

    allowed_fields = ["unordered_numbers", "ordered_numbers", "dna_sequence"]


    if field not in allowed_fields:
        return None


    file_path = Path.cwd() / file_name


    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)


    return data.get(field, None)


def linear_search(prohledavana_sekce, hledane_cislo_01):
    positions = []

    for idx, value in enumerate(prohledavana_sekce):
        if value == hledane_cislo_01:
            positions.append(idx)

    return {
        "positions": positions,
        "count": len(positions)
    }


def binary_search(prohledavany_seznam_cisel, hledane_cislo_02):
    left = 0
    right = len(prohledavany_seznam_cisel) - 1

    while left <= right:
        middle = (left + right) // 2

        if prohledavany_seznam_cisel[middle] == hledane_cislo_02:
            return middle
        elif prohledavany_seznam_cisel[middle] < hledane_cislo_02:
            left = middle + 1
        else:
            right = middle - 1

    return None


def main():

    sequential_data = read_data("sequential.json", "unordered_numbers")
    print("Unordered data:", sequential_data)

    hledane_cislo_number = 5
    linear_result = linear_search(sequential_data, hledane_cislo_number)
    print("Linear search:", linear_result)

    print("-" * 40)


    ordered_data = read_data("sequential.json", "ordered_numbers")
    print("Ordered data:", ordered_data)

    binary_result = binary_search(ordered_data, hledane_cislo_number)
    print("Binary search index:", binary_result)


if __name__ == "__main__":
    main()