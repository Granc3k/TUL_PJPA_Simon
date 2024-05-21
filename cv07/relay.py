"""
Modul pro zpracování výsledků závodu
"""

import json
import re
from bs4 import BeautifulSoup

# Názvy souborů
RESULTS_FILE = "result.html"
COMPETITORS_FILE = "competitors.json"
OUTPUT_FILE = "output.json"
ERRORS_FILE = "errors.txt"
COMPARE_FILE = "compare.txt"


def parse_html(file):
    """
    Funkce pro parsování HTML souboru
    """
    with open(file, "r", encoding="utf-8") as input_file:
        contents = input_file.read()

    # nalezení paragrafů
    paragraphs = BeautifulSoup(contents, "html.parser").find_all("p")
    relay_index = None
    for index, paragraph in enumerate(paragraphs):
        if "Relay" in paragraph.text:
            relay_index = index
            break

    if relay_index is None:
        print("Nenalezeny žádné výsledky štafet.")
        return []

    # rozparsování dat
    women = paragraphs[relay_index + 2].text.split(") ")
    men = paragraphs[relay_index + 4].text.split(") ")

    # zpracování dat
    data = {"women": [], "men": []}

    result = women[0]
    women.remove(women[0])

    for person in women:
        names = person.split(" (")[1].split(")")[0].split(", ")
        time = re.search(r"\d{1,2}:\d{2}:\d{2}", person)[0]
        for name in names:
            data["women"].append({"name": name, "time": time, "result": result})
        result = person.split(", ")[-1]

    result = men[0]
    men.remove(men[0])

    for person in men:
        names = person.split(" (")[1].split(")")[0].split(", ")
        time = re.search(r"\d{1,2}:\d{2}:\d{2}", person)[0]
        for name in names:
            data["men"].append({"name": name, "time": time, "result": result})
        result = person.split(", ")[-1]

    return data


def parse_json(file):
    """
    Funkce pro parsování JSON souboru
    """
    with open(file, "r", encoding="utf-8") as input_file:
        data = json.load(input_file)
    return data


def find_id(competitors, name):
    """
    Funkce pro hledání ID závodníka
    """
    for competitor in competitors:
        if competitor["firstname"] + " " + competitor["lastname"] == name:
            return competitor["id"]
    return False


def process_data(people, competitors):
    """
    Funkce pro zpracování dat
    """
    data = {"women": [], "men": []}
    for person in people["women"]:
        competitor_id = find_id(competitors, person["name"])
        if not competitor_id:
            data["women"].append(
                {
                    "id": competitor_id,
                    "time": person["time"],
                    "result": person["result"],
                    "no_match": person["name"],
                }
            )
        else:
            data["women"].append(
                {
                    "id": competitor_id,
                    "time": person["time"],
                    "result": person["result"],
                }
            )
    for person in people["men"]:
        competitor_id = find_id(competitors, person["name"])
        if not competitor_id:
            data["men"].append(
                {
                    "id": competitor_id,
                    "time": person["time"],
                    "result": person["result"],
                    "no_match": person["name"],
                }
            )
        else:
            data["men"].append(
                {
                    "id": competitor_id,
                    "time": person["time"],
                    "result": person["result"],
                }
            )
    return data


def write_errors(file, data):
    """
    Funkce pro zápis chyb do souboru
    """
    with open(file, "w", encoding="utf-8") as output_file:
        for person in data["women"]:
            if not person["id"]:
                output_file.write(f"{person['id']} {person['result']} {person['no_match']}\n")
        for person in data["men"]:
            if not person["id"]:
                output_file.write(f"{person['id']} {person['result']} {person['no_match']}\n")


def output_json(file, person_list):
    """
    Funkce pro zápis výsledků do JSON souboru
    """
    result_list = person_list["women"]+person_list["men"]
    with open(file, "w", encoding="utf-8") as output_file:
        output_file.write(json.dumps(result_list, indent=4, sort_keys=True))


def output_compare(file, data):
    """
    Funkce pro porovnání výsledků
    """
    with open(file, "w", encoding="utf-8") as output_file:
        for category in ["women", "men"]:
            for person in sorted(data[category], key=lambda x: x["id"]):
                if person["id"]:
                    output_file.write(f"{person['id']} {person['result']} {person['time']}\n")


def main():
    """
    Hlavní funkce
    """
    results = parse_html(RESULTS_FILE)
    competitors = parse_json(COMPETITORS_FILE)
    data = process_data(results, competitors)
    output_json(OUTPUT_FILE, data)
    output_compare(COMPARE_FILE, data)
    write_errors(ERRORS_FILE, data)


if __name__ == "__main__":
    main()
