import json
import glob

filepaths = glob.glob("./data/*.json")
full_list = []

for filepath in filepaths:
    with open(filepath, "r") as infile:
        lines = json.load(infile)
        full_list.extend(lines)

with open(f'slackmap.json', 'w') as outfile:
    json.dump(full_list, outfile)