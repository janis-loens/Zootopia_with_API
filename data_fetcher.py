import requests
import os
import json
from dotenv import load_dotenv

load_dotenv()  # lädt die .env-Datei

API_KEY = os.getenv("API_KEY")  # liest den Wert

FILEPATH = 'storage/animal_data.json'

def file_exists(file_path: str) -> bool:
    """Check if a file exists at the given path.
    Args:
        file_path (str): The path to the file.
    Returns:
        bool: True if the file exists, False otherwise.
    """
    return os.path.isfile(file_path)

def load_data(file_path: str) -> list[dict[str, str | list[str] | dict[str, str]]]:
    """Load data from a JSON file.
    Args:
        file_path (str): The path to the JSON file.
    Returns:
        list: A list of dictionaries containing the animal data.
    """
    with open(file_path, 'r') as handle:
        return json.load(handle)
    

def save_data(file_path: str, data: list) -> None:
    """Save data to a JSON file.
    Args:
        file_path (str): The path to the JSON file.
        data (list): The data to save.
    Returns:
        None
    """
    with open(file_path, 'w') as handle:
        json.dump(data, handle, indent=2)


def get_data(animal_name: str) -> dict[str, str | list[str] | dict[str, str]] | None:
    """Fetch animal information from the API by animal name.

    Args:
        animal_name (str): The name of the animal to search for.

    Returns:
        dict: A dictionary containing the animal's information if found.
        None: If the animal is not found or an error occurs.
    """
    local_data = load_data(FILEPATH) if file_exists(FILEPATH) else []
    animal_name_lower = animal_name.lower()

    # Check local data first
    for animal in local_data:
        if animal.get('name', '').lower() == animal_name_lower:
            return [animal]
        
    # If not found in local data, fetch from API
    api_url = 'https://api.api-ninjas.com/v1/animals?name={}'.format(animal_name)
    response = requests.get(api_url, headers={'X-Api-Key': API_KEY})
    # Check if the API request was successful
    if response.status_code == 200:
        api_data = response.json()
        if api_data:
            # If the animal is found in the API response, save it to local data
            local_data.extend(api_data)
            save_data(FILEPATH, local_data)
            return api_data
    elif response.status_code == 401:
        print("Error: Unauthorized — check your API key.")
    elif response.status_code == 400:
        print("Error: Bad request — maybe the API key is missing.")
    else:
        print(f"API request failed with status {response.status_code}: {response.text}")
    
    return None
    
def fetch_data(animal_name: str) -> list[dict[str, str | list[str] | dict[str, str]]] | None:
    """Fetch animal information either from the API or local data.
    Args:
        animal_name (str): The name of the animal to search for.
    Returns:
        list: A list of dictionaries containing the animal's information if found.
        None: If the animal is not found in both the API and local data.
    """
    
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
animals_to_fetch = [
    "Aardvark",
    "Albatross",
    "Alligator",
    "Alpaca",
    "Ant",
    "Anteater",
    "Antelope",
    "Ape",
    "Armadillo",
    "Donkey",
    "Baboon",
    "Badger",
    "Barracuda",
    "Bat",
    "Bear",
    "Beaver",
    "Bee",
    "Bison",
    "Boar",
    "Buffalo",
    "Butterfly",
    "Camel",
    "Capybara",
    "Caribou",
    "Cassowary",
    "Cat",
    "Caterpillar",
    "Cattle",
    "Chamois",
    "Cheetah",
    "Chicken",
    "Chimpanzee",
    "Chinchilla",
    "Chough",
    "Clam",
    "Cobra",
    "Cockroach",
    "Cod",
    "Cormorant",
    "Coyote",
    "Crab",
    "Crane",
    "Crocodile",
    "Crow",
    "Curlew",
    "Deer",
    "Dinosaur",
    "Dog",
    "Dogfish",
    "Dolphin",
    "Dotterel",
    "Dove",
    "Dragonfly",
    "Duck",
    "Dugong",
    "Dunlin",
    "Eagle",
    "Echidna",
    "Eel",
    "Eland",
    "Elephant",
    "Elk",
    "Emu",
    "Falcon",
    "Ferret",
    "Finch",
    "Fish",
    "Flamingo",
    "Fly",
    "Fox",
    "Frog",
    "Gaur",
    "Gazelle",
    "Gerbil",
    "Giraffe",
    "Gnat",
    "Gnu",
    "Goat",
    "Goldfinch",
    "Goldfish",
    "Goose",
    "Gorilla",
    "Goshawk",
    "Grasshopper",
    "Grouse",
    "Guanaco",
    "Gull",
    "Hamster",
    "Hare",
    "Hawk",
    "Hedgehog",
    "Heron",
    "Herring",
    "Hippopotamus",
    "Hornet",
    "Horse",
    "Human",
    "Hummingbird",
    "Hyena",
    "Ibex",
    "Ibis",
    "Jackal",
    "Jaguar",
    "Jay",
    "Jellyfish",
    "Kangaroo",
    "Kingfisher",
    "Koala",
    "Kookabura",
    "Kouprey",
    "Kudu",
    "Lapwing",
    "Lark",
    "Lemur",
    "Leopard",
    "Lion",
    "Llama",
    "Lobster",
    "Locust",
    "Loris",
    "Louse",
    "Lyrebird",
    "Magpie",
    "Mallard",
    "Manatee",
    "Mandrill",
    "Mantis",
    "Marten",
    "Meerkat",
    "Mink",
    "Mole",
    "Mongoose",
    "Monkey",
    "Moose",
    "Mosquito",
    "Mouse",
    "Mule",
    "Narwhal",
    "Newt",
    "Nightingale",
    "Octopus",
    "Okapi",
    "Opossum",
    "Oryx",
    "Ostrich",
    "Otter",
    "Owl",
    "Oyster",
    "Panther",
    "Parrot",
    "Partridge",
    "Peafowl",
    "Pelican",
    "Penguin",
    "Pheasant",
    "Pig",
    "Pigeon",
    "Pony",
    "Porcupine",
    "Porpoise",
    "Quail",
    "Quelea",
    "Quetzal",
    "Rabbit",
    "Raccoon",
    "Rail",
    "Ram",
    "Rat",
    "Raven",
    "Red deer",
    "Red panda",
    "Reindeer",
    "Rhinoceros",
    "Rook",
    "Salamander",
    "Salmon",
    "Sand Dollar",
    "Sandpiper",
    "Sardine",
    "Scorpion",
    "Seahorse",
    "Seal",
    "Shark",
    "Sheep",
    "Shrew",
    "Skunk",
    "Snail",
    "Snake",
    "Sparrow",
    "Spider",
    "Spoonbill",
    "Squid",
    "Squirrel",
    "Starling",
    "Stingray",
    "Stinkbug",
    "Stork",
    "Swallow",
    "Swan",
    "Tapir",
    "Tarsier",
    "Termite",
    "Tiger",
    "Toad",
    "Trout",
    "Turkey",
    "Turtle",
    "Viper",
    "Vulture",
    "Wallaby",
    "Walrus",
    "Wasp",
    "Weasel",
    "Whale",
    "Wildcat",
    "Wolf",
    "Wolverine",
    "Wombat",
    "Woodcock",
    "Woodpecker",
    "Worm",
    "Wren",
    "Yak",
    "Zebra"
]
for animal in animals_to_fetch:
    fetch_data(animal)