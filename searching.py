import os
import json

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



def main():
    pass


if __name__ == '__main__':
    main()
    sequential_data = read_data("sequential.json", "unordered numbers")
    print(sequential_data)