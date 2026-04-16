import time
import matplotlib.pyplot as plt
from generators import unordered_sequence, ordered_sequence
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

def measure_time(func, *args, repeat=5):
    times = []

    for _ in range(repeat):
        start = time.perf_counter()
        func(*args)
        end = time.perf_counter()
        times.append(end - start)

    return sum(times) / len(times)

def pattern_search(prohledavana_sekvence, hledany_vzor):

    positions = set()
    idx = 0

    while True:
        idx = prohledavana_sekvence.find(hledany_vzor, idx)

        if idx == -1:
            break

        positions.add(idx)
        idx += 1

    return positions

def main():

    sequential_data = read_data("sequential.json", "unordered_numbers")
    print("Unordered data:", sequential_data)

    hledane_cislo_number = 8
    linear_result = linear_search(sequential_data, hledane_cislo_number)
    print("Linear search:", linear_result)

    print("-" * 40)

    ordered_data = read_data("sequential.json", "ordered_numbers")
    print("Ordered data:", ordered_data)

    binary_result = binary_search(ordered_data, hledane_cislo_number)
    print("Binary search index:", binary_result)

    sizes = [100, 500, 1000, 5000, 10000]

    linear_times = []
    binary_times = []
    set_times = []

    target = 98

    for size in sizes:
        unordered = unordered_sequence(size)
        ordered = ordered_sequence(size)
        data_set = set(unordered)

        linear_t = measure_time(linear_search, unordered, target)
        binary_t = measure_time(binary_search, ordered, target)
        set_t = measure_time(lambda s, t: t in s, data_set, target)

        linear_times.append(linear_t)
        binary_times.append(binary_t)
        set_times.append(set_t)

    print(len(sizes), len(linear_times), len(binary_times), len(set_times))

    plt.figure(figsize=(10, 6))

    plt.plot(sizes, linear_times, marker="o", label="Linear search")
    plt.plot(sizes, binary_times, marker="o", label="Binary search")
    plt.plot(sizes, set_times, marker="o", label="Set membership")

    plt.xlabel("Velikost vstupu")
    plt.ylabel("Čas (s)")
    plt.title("Porovnání algoritmů")

    plt.legend()
    plt.grid()
    plt.yscale("log")

    plt.show()

    dna_sekvence = read_data("sequential.json", "dna_sequence")
    print("DNA sekvence:", dna_sekvence)

    hledany_vzor = "ATA"

    pozice_vyskytu = pattern_search(dna_sekvence, hledany_vzor)

    print("Pozice výskytu vzoru:", pozice_vyskytu)

if __name__ == "__main__":
    main()