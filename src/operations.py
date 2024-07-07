import json

def load_games(file_path):
    """
    Load games score from a JSON File.

    parameters: file_path: Path to the JSON file
    return: List of game scores or an empty list if an error occurs
    """
    try:
        with open(file_path, 'r') as file:
            games = json.load(file)
        return games
    except FileNotFoundError:
        print(f"Error: The file {file_path} does not exist.")
        return []
    except Exception as e:
        print(f"An unexpected error occured: {e}")
        return []
    
def save_games(file_path, games):
    try:
        with open(file_path, 'w') as file:
            json.dump(games, file, indent=4)
        print(f"Scores successfully saved to {file_path}.")
    except PermissionError:
        print(f"Error: Permission denied to write.")
    except Exception as e:
        print("An unexpected error occured", e)