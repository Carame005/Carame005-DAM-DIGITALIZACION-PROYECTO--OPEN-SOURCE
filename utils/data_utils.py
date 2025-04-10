import json
import os
from config import BASE_PATH

# Load keywords from a JSON file specific to the guild (server)
def load_keywords(guild_id):
    """
    Loads the keywords dictionary for the given guild from a JSON file.

    Args:
        guild_id (int): The Discord guild (server) ID.

    Returns:
        dict: A dictionary containing keywords and their responses.
    """
    guild_folder = os.path.join(BASE_PATH, str(guild_id))
    json_file = os.path.join(guild_folder, "keywords.json")

    if os.path.exists(json_file):
        with open(json_file, "r") as f:
            return json.load(f)
    return {}

# Save keywords to a JSON file specific to the guild (server)
def save_keywords(guild_id, keywords):
    """
    Saves the keywords dictionary for the given guild to a JSON file.

    Args:
        guild_id (int): The Discord guild (server) ID.
        keywords (dict): The dictionary of keywords and responses to save.
    """
    guild_folder = os.path.join(BASE_PATH, str(guild_id))
    json_file = os.path.join(guild_folder, "keywords.json")

    os.makedirs(guild_folder, exist_ok=True)
    with open(json_file, "w") as f:
        json.dump(keywords, f, indent=4)
