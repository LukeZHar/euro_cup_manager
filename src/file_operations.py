import json

def load_matches(file_path):
    """
    Load matches from JSON file
    
    parameters: file_path: Path to JSON file

    returns: List of matches or an empty list if an error occurs
    """

    try:
        with open(file_path, 'r') as file:
            matches = json.load(file)
        return matches
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []
    
def save_matches(file_path, matches):
    """
    Save matches to JSON file
    
    parameters: file_path: Path to JSON file
                matches: List of matches
    """

    try:
        with open(file_path, 'w') as file:
            json.dump(matches, file, indent=4)
        print(f"Matches saved to {file_path}")
    except PermissionError:
        print(f"Permission denied to write")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

