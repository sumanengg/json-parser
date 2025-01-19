import sys

from .jsonparser import JsonValidator


def cli(filename: str):
    validator = JsonValidator()
    if validator.is_valid_simple_json(filename):
        print(f"{filename} is valid JSON")
    else:
        print(f"{filename} is not valid JSON")


if __name__ == "__main__":
    json_file = sys.argv[1]
    cli(json_file)
