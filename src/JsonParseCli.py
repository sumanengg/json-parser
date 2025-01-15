import sys

from .jsonparser import JsonValidator


def cli(filename: str):
    validator = JsonValidator()
    
    try:
        if validator.is_valid_simple_json(filename):
            print(f"{filename} is a valid json file")
        else:
            print(f"{filename} is not a valid json file")
            sys.exit(1)
    except Exception as e:
        print(f"Got failed due to {e}")
        sys.exit(1)


if __name__ == "__main__":
    json_file = sys.argv[1]
    cli(json_file)
