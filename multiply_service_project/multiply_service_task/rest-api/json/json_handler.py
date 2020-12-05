from json import load, dumps

from nested_diff import diff


def read_json_file(path: str) -> dict:
    with open(path) as json_file:
        return load(json_file)


def get_different_between_two_files(first_json_file: load, second_json_file: load) -> dict:
    different = diff(first_json_file, second_json_file)
    return different


def get_json_human_readable(first_json_file: load, second_json_file: load) -> str:
    different = diff(first_json_file, second_json_file)
    return dumps(different, indent=2)