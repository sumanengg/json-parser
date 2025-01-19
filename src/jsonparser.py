import io
from .JsonParseError import JsonParseerror


class JsonValidator:
    """
    A validator for JSON files.
    """

    def __init__(self):
        self._token = ""
        self._line = 1
        self._column = 0
        self._file = None

    def _raise_error(self, message: str):
        raise JsonParseerror(f"Error: {message} at line {self._line}, column {self._column}")

    def _get_next_char(self):
        char = self._file.read(1)
        if char == "\n":
            self._line += 1
            self._column = 0
        else:
            self._column += 1
        return char

    def _skip_whitespace(self):
        """Skips over whitespace and updates the token."""
        while True:
            char = self._get_next_char()
            if char not in [" ", "\t", "\n", "\r"]:
                self._token = char
                return char

    def _parse_string(self):
        """Parses a string from the file."""
        result = ""
        if self._token != '"':
            self._raise_error('Expected \'"\' to start a string')

        while True:
            char = self._get_next_char()
            if char == '"':
                self._token = self._get_next_char()  # Read the next character after the string
                return result
            elif char == "":
                self._raise_error("Unexpected end of file in string")
            elif char == "\\":
                # Handle escape characters
                char = self._get_next_char()
                if char in ['"', "\\", "/", "b", "f", "n", "r", "t"]:
                    result += char
                else:
                    self._raise_error(f"Invalid escape sequence: \\{char}")
            else:
                result += char

    def _parse_key_value_pair(self):
        """Parses a key-value pair from the file."""
        key = self._parse_string()
        if self._token != ":":
            self._raise_error("Expected ':' after key")
        self._token = self._get_next_char()  # Skip the ':'
        self._skip_whitespace()
        value = self._parse_string()  # Assumes values are strings for this simple validator
        return key, value

    def _parse_object(self):
        """Parses a JSON object."""
        obj = {}
        if self._token != '{':
            self._raise_error("Expected '{' to start an object")

        self._token = self._get_next_char()  # Consume '{'
        self._skip_whitespace()

        if self._token == '}':
            return obj  # Empty object

        while True:
            key, value = self._parse_key_value_pair()
            obj[key] = value
            print(f"Key: {key}, Value: {value}")

            self._skip_whitespace()
            print(f"Token1: {self._token}")
            if self._token == '}':
                self._token = self._get_next_char()  # Consume '}'
                return obj
            elif self._token != ',':
                self._raise_error("Expected ',' or '}' in object")
            print(f"Token2: {self._token}")
            self._token = self._get_next_char()  # Consume ',' and continue

    def open_file(self, filename: str):
        """Opens a file for JSON validation."""
        if not filename or "." not in filename:
            self._raise_error("No file specified")
        if not filename.endswith(".json"):
            self._raise_error("Invalid file type")
        try:
            self._file = open(filename, "r", encoding="UTF-8")
        except FileNotFoundError as e:
            self._raise_error(str(e))

    def close_file(self):
        if self._file:
            self._file.close()

    def is_valid_simple_json(self, filename: str) -> bool:
        try:
            self.open_file(filename)
            self._token = self._skip_whitespace()
            if self._token != '{':
                self._raise_error("JSON must start with '{'")
            self._parse_object()
            self.close_file()
            return True
        except JsonParseerror as e:
            print(f"Validation failed: {e}")
            return False
        except Exception as e:
            print(f"Unexpected error: {e}")
            return False
