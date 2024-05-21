"""
Module for text censorship.
"""
import argparse
import re
from bs4 import BeautifulSoup

def input_parse():
    """
    Parsing form console.
    """
    parser = argparse.ArgumentParser(description='Censorship of selected words.')
    parser.add_argument("-i", "--input", metavar="", required=True, help="file to censor")
    parser.add_argument("-l", "--list", metavar="",
        required=True, help="file with list of censored words")
    parser.add_argument("-c", "--clean", action="store_true", help="clear html marks")
    parser.add_argument("-o", "--output", metavar="",
        help="output file (if not selected, program will print the result to console")

    return parser.parse_args()

def load_input(file_name):
    """
    Loading lines from a file.
    """
    with open(file_name, "r", encoding="utf-8") as file:
        return file.read()

def clean_html(input_data):
    """
    Removing HTML parts from text.
    """
    soup = BeautifulSoup(input_data, 'html.parser')
    return soup.get_text()

def print_censored_text(data, output_file):
    """
    Checking parameter c and selecting printing to file or console.
    """
    if output_file is None:
        print_to_console(data)
    else:
        print_to_file(data, output_file)

def censor(data, censor_list):
    """
    Replacing selected words by #s.
    """
    for word in censor_list:
        data = re.sub(r'\b' + word + r'\b', '#' * len(word), data, flags=re.IGNORECASE)
    return data

def print_to_console(data):
    """
    Printing lines to console.
    """
    print(data)

def print_to_file(data, file_name):
    """
    Printing lines to selected file.
    """
    with open(file_name, "w+", encoding="utf-8") as file:
        file.write(data)

def main():
    """
    Main body of code created primarily for testing.
    """
    requested_task = input_parse()
    input_text = load_input(requested_task.input)
    censor_words = load_input(requested_task.list).splitlines()

    if requested_task.clean:
        input_text = clean_html(input_text)

    censored_text = censor(input_text, censor_words)

    print_censored_text(censored_text, requested_task.output)

if __name__ == '__main__':
    main()
