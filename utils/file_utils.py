import os

# Directory management utility
def ensure_directory_exists(directory):
    """
    Ensures that a directory exists. Creates it if it does not.

    Args:
        directory (str): The path of the directory to check or create.
    """
    if not os.path.exists(directory):
        os.makedirs(directory)
