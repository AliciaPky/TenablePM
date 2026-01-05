import json
from config import JSON_OUTPUT_PATH

def save_to_json(data):
    with open(JSON_OUTPUT_PATH, "w") as f:
        json.dump(data, f, indent=4)
