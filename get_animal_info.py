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