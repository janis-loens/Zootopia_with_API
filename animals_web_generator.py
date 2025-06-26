import os.path
from data_fetcher import fetch_data


def file_exists(file_path: str) -> bool:
    """Check if a file exists at the given path.
    Args:
        file_path (str): The path to the file.
    Returns:
        bool: True if the file exists, False otherwise.
    """
    return os.path.isfile(file_path)

    
def get_data(data: list[dict[str, str | list[str] | dict[str, str]]]) -> str:
    """Generate a string with information about animals.

    Args:
        data: A list of dictionaries containing animal data.

    Returns:
        A formatted HTML string with information about each animal.
    """
    animals = ''

    for animal in data:
        name = animal.get('name', 'Unknown')

        # Ensure characteristics is a dict
        characteristics_raw = animal.get('characteristics', {})
        characteristics = characteristics_raw if isinstance(characteristics_raw, dict) else {}

        diet = characteristics.get('diet', 'Unknown')
        type_ = characteristics.get('type')

        # Ensure locations is a list
        locations_raw = animal.get('locations', [])
        locations = locations_raw if isinstance(locations_raw, list) else []
        location = locations[0] if locations else 'Unknown'

        animals += (
            '<li class="cards__item">\n'
            f'  <div class="card__title">{name}</div>\n'
            '  <div class="card__text">\n'
            '    <ul>\n'
            f'      <li><strong>Diet:</strong> {diet}</li>\n'
            f'      <li><strong>Location:</strong> {location}</li>\n'
        )

        if type_:
            animals += f'      <li><strong>Type:</strong> {type_}</li>\n'

        animals += (
            '    </ul>\n'
            '  </div>\n'
            '</li>\n'
        )

    return animals


def read_html(file_path: str) -> str:
    """Read the content of an HTML file.
    Args:
        file_path (str): The path to the HTML file.
    Returns:
        str: The content of the HTML file.
    """
    with open(file_path, 'r') as file:
        return file.read()


def update_html_string(html_content: str, data: str) -> str:
    """Update the HTML content with the provided data.
    Args:
        html_content (str): The original HTML content.
        data (str): The data to insert into the HTML.
    Returns:
        str: The updated HTML content.
    """
    return html_content.replace('__REPLACE_ANIMALS_INFO__', data)


def error_html(html_content: str, animal: str) -> str:
    """Update the HTML content with the provided data.
    Args:
        html_content (str): The original HTML content.
        data (str): The data to insert into the HTML.
    Returns:
        str: The updated HTML content.
    """
    error_message = f'<h2>No data found for {animal}.</h2>'
    return html_content.replace("""<ul class="cards">
            __REPLACE_ANIMALS_INFO__
        </ul>""", error_message)


def update_html(file_path: str, updated_html_string: str) -> None:
    """Create or overwrite the html file with the updated version.
    Args:
        file_path (str): The path to the HTML file to be created or updated.
        updated_html_string (str): The updated HTML content.
    Returns:
        None
    """
    with open(file_path, 'w') as file:
        file.write(updated_html_string)

def main():
    """Load animal data from a JSON file, generate a string with foxes information,
    read an HTML template, update it with the foxes information, and save the updated HTML.
    Raises:
        FileNotFoundError: If the JSON or HTML template file does not exist.
    """

    if not file_exists('animals_template.html'):
            raise FileNotFoundError('The file "animals_template.html" does not exist.')
    html_data = read_html('animals_template.html')
    animal = input('Enter the name of the animal to search for (e.g., "fox"): ').strip().lower()
    animals_data = fetch_data(animal)

    if not animals_data:
        error_message = error_html(html_data, animal)
        update_html('animals.html', error_message)
        print(f'No data found for {animal}. HTML file "animals.html" has been updated with an error message.')

    else:
        animal_data = get_data(animals_data)
        updated_html = update_html_string(html_data, animal_data)
        update_html('animals.html', updated_html)
        print(f'HTML file "animals.html" has been successfully updated with {animal} data.')
if __name__ == '__main__':
    main()