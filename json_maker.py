# Copyright (C) 2023 by Nikodem "Med0kin" Kuliś
# This file is part of the intentsCreator project,
# and is released under the "MIT License Agreement".
# Please see the LICENSE file that should have been included
# as part of this package.

import json


def new_json() -> dict:
    intents = {
        "intents": []
    }
    return intents


def import_json(file_name: str) -> dict:
    with open(file_name, encoding='utf-8') as f:
        intents = json.load(f)
    existing_tags = [intent['tag'] for intent in intents['intents']]
    return intents


def export_json(file_name: str, intents: dict) -> None:
    with open(file_name, 'w', encoding='utf-8') as f:
        json.dump(intents, f, indent=4, ensure_ascii=False)


def add_tag(intents: dict, tag: str) -> dict:
    existing_tags = [intent['tag'] for intent in intents['intents']]
    if tag not in existing_tags:
        existing_tags.append(tag)
        # append tag, pattern and response to intents
        intents["intents"].append(
            {"tag": tag,
             "patterns": [],
             "responses": [],
             "context_set": ""}
            )
        return intents
    return False


def add_pattern(intents: dict, tag: str, pattern: str) -> dict:
    add_tag(intents, tag)
    # find the tag in intents
    for intent in intents["intents"]:
        if intent["tag"] == tag:
            # check if pattern already exists
            if pattern not in intent["patterns"]:
                intent["patterns"].append(pattern)
                return intents
    # return intents if pattern already exists
    return intents



def add_response(intents: dict, tag: str, response: str) -> dict:
    add_tag(intents, tag)
    # find the tag in intents
    for intent in intents["intents"]:
        if intent["tag"] == tag:
            # check if pattern already exists
            if response not in intent["responses"]:
                intent["responses"].append(response)
                return intents
    # return intents if pattern already exists
    return intents


def delete_tag(intents: dict, tag: str) -> dict:
    # find the tag in intents
    for intent in intents["intents"]:
        if intent["tag"] == tag:
            # delete tag
            intents["intents"].remove(intent)
            return intents
    # return intents if tag not exists
    return intents


def delete_pattern(intents: dict, tag: str, pattern: str) -> dict:
    # find the tag in intents
    for intent in intents["intents"]:
        if intent["tag"] == tag:
            # delete pattern
            intent["patterns"].remove(pattern)
            return intents
    # return intents if tag not exists
    return intents


def delete_response(intents: dict, tag: str, response: str) -> dict:
    # find the tag in intents
    for intent in intents["intents"]:
        if intent["tag"] == tag:
            # delete response
            intent["responses"].remove(response)
            return intents
    # return intents if tag not exists
    return intents


if __name__ == '__main__':
    # create new json file
    intents = new_json()
    intents = add_tag(intents, "greewting")
    intents = add_pattern(intents, "greeting", "hello there")
    intents = add_pattern(intents, "greeting", "howdy")
    intents = add_response(intents, "greeting", "Hello, thanks for asking")
    intents = add_response(intents, "greeting", "Hello, thanks for asking")
    intents = delete_pattern(intents, "greeting", "howdy")
    # write to json file
    with open("intents.json", "w", encoding="utf-8") as f:
        json.dump(intents, f, indent=4, ensure_ascii=False)
