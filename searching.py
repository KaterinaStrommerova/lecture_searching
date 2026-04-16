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


def linear_search(sequence, target):
    positions = []

    for idx, value in enumerate(sequence):
        if value == target:
            positions.append(idx)

    return {
        "positions": positions,
        "count": len(positions)
    }


def main():

    sequential_data = read_data("sequential.json", "unordered_numbers")
    print("Data:", sequential_data)


    if sequential_data is None:
        print("Chyba, data nejsou k dispozici.")
        return

    target_number = 5

    result = linear_search(sequential_data, target_number)

    print("Výsledek hledání:", result)


if __name__ == "__main__":
    main()