import os
import json

from setuptools.dist import sequence

# get current working directory path
cwd_path = os.getcwd()

def read_data(file_name, field):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """
    file_path = os.path.join(cwd_path, file_name)
    with open(file_path, "r") as file_obj:
        data = json.load(file_obj)

    if field in data.keys():
        return data[field]
    else:
        print(f"Field {field} not exist!")
        return None

def linear_search(sequence, number):
    list_of_idxs = []
    for idx, num in enumerate(sequence):
        if num == number:
            list_of_idxs.append(idx)
        else:
            pass
    return {"positions": list_of_idxs, "count": len(list_of_idxs)}

def pattern_search(sequence, pattern):
    set_of_idxs = set()
    pattern_length = len(pattern)
    for idx in range(0, len(sequence)-pattern_length):
        pattern_similarity = 0
        for idx_pattern, pattern_element in enumerate(pattern):
            if sequence[idx + idx_pattern] == pattern_element:
                pattern_similarity += 1
            else:
                break
        if pattern_similarity == pattern_length:
            set_of_idxs.add(idx + pattern_length // 2 - 1)
        else:
            pass
    return set_of_idxs

def binary_search(sequence, number):
    left = 0
    right = len(sequence) - 1
    while right >= left:
        middle = (left + right) // 2
        print(sequence[middle])
        if sequence[middle] == number:
            return middle
        elif sequence[middle] > number:
            right = middle - 1
        elif sequence[middle] < number:
            left = middle + 1
    return None


def main():
    file_name = "sequential.json"
    key_of_sequence = "dna_sequence"
    sequential_data = read_data("sequential.json", "unordered_numbers")
    print(sequential_data)
    found_numbers = linear_search(sequential_data, 0)
    print(found_numbers)


if __name__ == '__main__':
    binary_search(read_data("sequential.json", "ordered_numbers"), 5)
