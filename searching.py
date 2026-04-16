from pathlib import Path
import json


def read_data(file_name, field):
    """
    Reads a JSON file and returns data for a given field.

    Args:
        file_name (str): Name of the JSON file.
        field (str): Key to retrieve from the JSON data.
            Must be one of: 'unordered_numbers', 'ordered_numbers' or 'dna_sequence'.

    Returns:
        list | str | None:
    """
    # get current working directory path
    cwd_path = Path.cwd()
    file_path = cwd_path / file_name

    # otevření a načtení JSON
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)

    # kontrola povolených polí
    if field not in ["unordered_numbers", "ordered_numbers", "dna_sequence"]:
        return None

    # vrácení hodnoty
    return data.get(field, None)


def main():
    print(read_data("sequential.json", "unordered_numbers"))
    print(read_data("sequential.json", "dna_sequence"))


if __name__ == "__main__":
    main()