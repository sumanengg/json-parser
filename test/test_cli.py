import unittest
from src.jsonparser import JsonValidator

class TestJSONValidator(unittest.TestCase):
    def setUp(self):
        """
        Set up test data before each test case runs.
        """
        self.validator = JsonValidator()

    def test_valid_json(self):
        """
        Test case for valid JSON object '{}'.
        """
        valid_json = "{}"
        self.assertTrue(self.validator.is_valid_simple_json(valid_json), "Should return True for '{}'")

    def test_invalid_json_extra_characters(self):
        """
        Test case for invalid JSON with extra characters.
        """
        invalid_json = "{abc}"
        self.assertFalse(self.validator.is_valid_simple_json(invalid_json), "Should return False for '{abc}'")

    def test_invalid_json_empty_string(self):
        """
        Test case for an empty string.
        """
        empty_json = ""
        self.assertFalse(self.validator.is_valid_simple_json(empty_json), "Should return False for an empty string")

    def test_invalid_json_with_whitespace(self):
        """
        Test case for strings with only whitespace.
        """
        whitespace_json = "   "
        self.assertFalse(self.validator.is_valid_simple_json(whitespace_json), "Should return False for whitespace-only strings")

    def test_invalid_json_with_mismatched_braces(self):
        """
        Test case for invalid JSON with mismatched braces.
        """
        mismatched_json = "{"
        self.assertFalse(self.validator.is_valid_simple_json(mismatched_json), "Should return False for '{'")

    def test_invalid_json_with_special_characters(self):
        """
        Test case for invalid JSON with special characters.
        """
        special_characters_json = "{@}"
        self.assertFalse(self.validator.is_valid_simple_json(special_characters_json), "Should return False for '{@}'")

    def test_valid_json_with_whitespace(self):
        """
        Test case for valid JSON object '{}' with leading/trailing whitespace.
        """
        valid_json_with_whitespace = "  {}  "
        self.assertTrue(self.validator.is_valid_simple_json(valid_json_with_whitespace), "Should return True for '  {}  '")

if __name__ == "__main__":
    unittest.main()
