import json
import os.path

def file_exists(file_path: str) -> bool:
    """Check if a file exists at the given path.
    Args:
        file_path (str): The path to the file.
    Returns:
        bool: True if the file exists, False otherwise.
    """
    return os.path.isfile(file_path)

def load_data(file_path) -> list:
    """Load data from a JSON file."""
    with open(file_path, 'r') as handle:
        return json.load(handle)
    
def get_data(data) -> str:
    """Generate a string with information about foxes.
    Args:
        data (list): A list of dictionaries containing animal data.
    Returns:
        str: A formatted string with information about each fox.
    """
    animals = ''
    for animal in data:
        name = animal.get('name', 'Unknown')
        characteristics = animal.get('characteristics', {})
        diet = characteristics.get('diet', 'Unknown')
        type_ = characteristics.get('type')  # None if missing
        locations = animal.get('locations', [])
        location = locations[0] if locations else 'Unknown'

        animals += f'<li class="cards__item">\n<div class="card__title">{name}</div>\n<div class="card__text">\n<ul>\n'
        animals += f'<li>\n<strong>Diet:</strong> {diet}\n</li>\n'
        animals += f'<li>\n<strong>Location:</strong> {location}\n</li>\n'
        if type_:
            animals += f'<li>\n<strong>Type:</strong> {type_}\n</li>\n'
        animals += '</ul>\n</div>\n</li>\n'
    return animals

def read_html(file_path) -> str:
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

    if not file_exists('animals_data.json'):
        raise FileNotFoundError('The file "animals_data.json" does not exist.')

    animals_data = load_data('animals_data.json')
    foxes_data = get_data(animals_data)
    if not file_exists('animals_template.html'):
        raise FileNotFoundError('The file "animals_template.html" does not exist.')
    html_data = read_html('animals_template.html')
    updated_html = update_html_string(html_data, foxes_data)
    update_html('animals.html', updated_html)
    print('HTML file "animals.html" has been successfully updated with foxes data.')

if __name__ == '__main__':
    main()
