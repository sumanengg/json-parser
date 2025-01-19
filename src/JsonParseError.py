class JsonParseerror(Exception):
    """
    Exception raised for errors in the JSON parsing process.

    Attributes:
        message -- explanation of the error
    """
    def __init__(self, *args):
        super().__init__(*args)