import requests
import os
import json
from dotenv import load_dotenv

load_dotenv()  # lädt die .env-Datei

API_KEY = os.getenv("API_KEY")  # liest den Wert

FILEPATH = 'animal_data.json'

def file_exists(file_path: str) -> bool:
    """Check if a file exists at the given path.
    Args:
        file_path (str): The path to the file.
    Returns:
        bool: True if the file exists, False otherwise.
    """
    return os.path.isfile(file_path)

def load_data(file_path: str) -> list[dict[str, str | list[str] | dict[str, str]]]:
    """Load data from a JSON file."""
    with open(file_path, 'r') as handle:
        return json.load(handle)


def get_data(animal_name: str) -> dict[str, str | list[str] | dict[str, str]] | None:
    """Fetch animal information from the API by animal name.

    Args:
        animal_name (str): The name of the animal to search for.

    Returns:
        dict: A dictionary containing the animal's information if found.
        None: If the animal is not found or an error occurs.
    """

    api_url = 'https://api.api-ninjas.com/v1/animals?name={}'.format(animal_name)
    response = requests.get(api_url, headers={'X-Api-Key': API_KEY})

    if response.status_code == 200:
        return response.json()
    elif response.status_code == 401:
        print("Error: Unauthorized — check your API key.")
    elif response.status_code == 400:
        print("Error: Bad request — maybe the API key is missing.")
    else:
        print(f"API request failed with status {response.status_code}: {response.text}")
    
    return None
    
def fetch_data(animal_name: str) -> list[dict[str, str | list[str] | dict[str, str]]] | None:
    
    animal_info = get_data(animal_name)

    if animal_info:
        print(f"Information for {animal_name} fetched from API")
        return animal_info
    
    else:
        print(f"Could not fetch from API. Trying local data for '{animal_name}'")
        if file_exists(FILEPATH):
            try:
                local_data = load_data(FILEPATH)
                chosen_animal_info = next(
                    (animal for animal in local_data if animal_name.lower() in animal.get('name', '').lower()),
                    None
                )
                if chosen_animal_info:
                    print("Data loaded from local file.")
                    return [chosen_animal_info]
                else:
                    print(f"No information found for {animal_name} in local data.")
            except Exception as e:
                print(f"Failed to load local data: {e}")
        else:
            print("No local data file found.")
        return None

if __name__ == "__main__":
   fetch_data()