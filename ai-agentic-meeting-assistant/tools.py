from pathlib import Path
import json


def get_client_profile(client_name):

    path = Path("data/acme_profile.txt")

    return path.read_text()


def get_meeting_notes(client_name):

    path = Path("data/acme_meeting_notes.txt")

    return path.read_text()


def get_action_items(client_name):

    path = Path("data/acme_action_items.txt")

    return path.read_text()


def get_long_term_memory(client_name):

    with open(
        "memory/long_term_memory.json",
        "r"
    ) as f:

        memory = json.load(f)

    return memory.get(
        client_name,
        {}
    )
