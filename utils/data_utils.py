import json
import os
from config import BASE_PATH
    #Json load
def load_keywords(guild_id):
    guild_folder = os.path.join(BASE_PATH, str(guild_id))
    json_file = os.path.join(guild_folder, "keywords.json")

    if os.path.exists(json_file):
        with open(json_file, "r") as f:
            return json.load(f)
    return {}
    #Json save
def save_keywords(guild_id, keywords):
    guild_folder = os.path.join(BASE_PATH, str(guild_id))
    json_file = os.path.join(guild_folder, "keywords.json")

    os.makedirs(guild_folder, exist_ok=True)
    with open(json_file, "w") as f:
        json.dump(keywords, f, indent=4)
