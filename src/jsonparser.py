import io
from JsonParseError import JsonParseerror


class JsonValidator:
    """
    A validator for Json files
    """
    def __int__(self):
        self._token = ""
        self._line = 0
        self._column = 0

    def _raise_error(self, message: str):
        raise JsonParseerror(message)
    
    def _get_next_char(self):
        pass



    def open_file(self, filename: str):
        """ Opens a file for JSON validation.

        Sets the initial _line number and column number then gets the first column.

        Args:
            filename (str): The name of the file to be opened.

        Raises:
            JSONValidatorError: An exception with error message, error code, line number, and column number
        """
        # check for no file provided
        if not filename or "." not in filename:
            self._raise_error("no file specified")
        # check for invalid file type
        if not filename.endswith(".json"):
            self._raise_error("invalid file type")
        try:
            self._file = open(filename, "r", encoding="UTF-8")
        except FileNotFoundError as e:
            self._raise_error(str(e))

    def close_file(self):
        self._file.close()
    
    def is_valid_simple_json(self, filename: str) -> bool:
        try:
            self.open_file(filename)
            content = self._file.read()
            print(content)
        
            self.close_file()
            return content == "{}"
        except JsonParseerror as e:
            return False


