import csv
import json
from pprint import pprint


def save_as_json(data):
    with open("./bremene-gruppen.json", "w") as outfile:
        json.dump(data, outfile, indent=2, ensure_ascii=False)


def main():
    collected = {}
    had_dash = False
    current_number = 0
    with open("./tabula-Bremen-Gruppen.csv") as infile:
        reader = csv.reader(infile)
        for line in reader:
            if line[0] != "":
                current_number = line[0]
                title = line[1]
                if title.endswith("-"):
                    had_dash = True
                    title = title[:-1]
                else:
                    had_dash = False
                collected[current_number] = title
                continue

            if had_dash:
                collected[current_number] += line[1]
            else:
                collected[current_number] += " " + line[1]

    pprint(collected)
    save_as_json(collected)


if __name__ == '__main__':
    main()
