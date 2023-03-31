import json
import argparse


def merge_intents(intents_file1, intents_file2, merged_file):
    # Load the intent data from the first JSON file
    with open(intents_file1, encoding='utf-8') as f1:
        intents1 = json.load(f1)

    # Load the intent data from the second JSON file
    with open(intents_file2, encoding='utf-8') as f2:
        intents2 = json.load(f2)

    # List of tags that exist in the first JSON file
    tags1 = [intent['tag'] for intent in intents1['intents']]

    # Merge the two intent data dictionaries
    for dict1 in intents1['intents']:
        for dict2 in intents2['intents']:
            if dict1['tag'] == dict2['tag']:
                for i in dict2['patterns']:
                    if i not in dict1['patterns']:
                        dict1['patterns'].append(i)
                for i in dict2['responses']:
                    if i not in dict1['responses']:
                        dict1['responses'].append(i)
            if dict2['tag'] not in tags1:
                intents1['intents'].append(dict2)
                tags1.append(dict2['tag'])
        

    # Write the merged intent data to a new JSON file with UTF-8 encoding
    with open(merged_file, 'w', encoding='utf-8') as f3:
        json.dump(intents1, f3, indent=4, ensure_ascii=False)

if __name__ == '__main__':
    file1 = "intents1.json"
    file2 = "intents2.json"
    output = "merged_intents.json"

    # Merge json files
    merge_intents(file1, file2, output)

    print("Done!")