import unittest
from censor import input_parse, print_to_console, print_censored_text, censor
from io import StringIO
import io
import sys
import os

class TestInputParse(unittest.TestCase):
    def test_censor_single_word(self):
        data = "This is a test sentence."
        censor_list = ["test"]
        expected_output = "This is a #### sentence."
        self.assertEqual(censor(data, censor_list), expected_output)

    def test_censor_multiple_words(self):
        data = "This is a test sentence with multiple test words."
        censor_list = ["test", "words"]
        expected_output = "This is a #### sentence with multiple #### #####."
        self.assertEqual(censor(data, censor_list), expected_output)

    def test_censor_case_insensitive(self):
        data = "This is a Test sentence."
        censor_list = ["test"]
        expected_output = "This is a #### sentence."
        self.assertEqual(censor(data, censor_list), expected_output)
    
    def test_print_to_console(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        print_to_console("Hello, World!")
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue().strip(), "Hello, World!")


if __name__ == '__main__':
    unittest.main()