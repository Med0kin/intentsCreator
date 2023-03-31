#program that creates intents.json file based on given data

import json

intents = {
    "intents": []}

existing_tags = []

def import_json(file_name):
    with open(file_name, encoding='utf-8') as f:
        intents = json.load(f)
    existing_tags = [intent['tag'] for intent in intents['intents']]

def export_json(file_name):
    with open(file_name, 'w', encoding='utf-8') as f:
        json.dump(intents, f3, indent=4, ensure_ascii=False)


def add_tag(tag):
    if tag not in existing_tags:
        existing_tags.append(tag)
        # append tag, pattern and response to intents
        intents["intents"].append({"tag": tag, "patterns": [], "responses": [], "context_set": ""})
        return True
    return False

def add_pattern(tag, pattern):
    add_tag(tag)
    # find the tag in intents
    for intent in intents["intents"]:
        if intent["tag"] == tag:
            # check if pattern already exists
            if pattern not in intent["patterns"]:
                intent["patterns"].append(pattern)
                return True
    return False

def add_response(tag, response):
    add_tag(tag)
    # find the tag in intents
    for intent in intents["intents"]:
        if intent["tag"] == tag:
            # check if pattern already exists
            if response not in intent["responses"]:
                intent["responses"].append(response)
                return True
    return False

if __name__ == '__main__':
    add_pattern("greeting", "hello there")
    add_pattern("hello", "hi")
    add_pattern("greeting", "how are you")
    add_pattern("greeting", "how are you")
    print(intents["intents"])
    print(existing_tags)
    # write to json file
    with open("intents.json", "w", encoding="utf-8") as f:
        json.dump(intents, f, indent=4, ensure_ascii=False)

        