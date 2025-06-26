import requests

def get_animal_info(animal_name: str) -> dict[str, str | list[str] | dict[str, str]] | None:
    """Fetch animal information from the API by animal name.

    Args:
        animal_name (str): The name of the animal to search for.

    Returns:
        dict: A dictionary containing the animal's information if found.
        None: If the animal is not found or an error occurs.
    """

    api_url = 'https://api.api-ninjas.com/v1/animals?name={}'.format(animal_name)
    response = requests.get(api_url, headers={'X-Api-Key': 'dNDKd0rbYiX7/LSq+JuLKQ==o7TAopY1H9nkSa7n'})
    if response.status_code == requests.codes.ok:
        return response.json()
    else:
        print("Error:", response.status_code, response.text)
        return None
    
def main():
    animal_name = input("Enter the name of the animal: ")
    animal_info = get_animal_info(animal_name)
    
    if animal_info:
        print(f"Information for {animal_name}:")
        print(animal_info)
    else:
        print(f"No information found for {animal_name}.")

if __name__ == "__main__":
    main()