# 🐾 My Zootopia API

Welcome to the **My Zootopia API** project — a Python-based tool to fetch and store animal data for use in a simple web interface.

## 🚀 Features

- Fetches detailed animal information from an external API.
- Saves data to a local `animal_data.json` as a backup in case the API is unavailable.
- Generates HTML pages displaying animal data using a Jinja2 template.
- Uses environment variables for secure API key management.
- Modular, easy-to-understand code structure.

## 🐍 Tech Stack

- Python 3.11+
- `requests` – for API access
- `Jinja2` – for HTML templating
- `.env` support via `os.environ`

## 📁 Project Structure

```
My-Zootopia-API/
│
├── animals_web_generator.py     # Main script to generate HTML from data
├── data_fetcher.py              # Handles data fetching and saving
├── storage/
│   └── animal_data.json         # Local JSON backup of animal records
├── html/
│   ├── animals_template.html    # HTML template with a placeholder
│   └── animals.html             # Output HTML file
├── .env                         # Your API key goes here
├── requirements.txt             # Python dependencies
└── README.md                    # This file
```

## 🔐 Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/janis-loens/My-Zootopia.git
   cd My-Zootopia-API
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Add your API key to a `.env` file:
   ```
   API_KEY=your_api_key_here
   ```

4. Run the program:
   ```bash
   python animals_web_generator.py
   ```

## 🧪 Testing

No automated tests yet — manual testing via console output and generated HTML is used.

## 📄 License

MIT License. Free to use and modify.

---

## ✨ Future Ideas

- Add a simple Flask frontend.
- Add unit tests with `pytest`.
- Add search/filter features to the HTML.

---

If this project helped you, leave a ⭐ on GitHub or fork it to build your own version!