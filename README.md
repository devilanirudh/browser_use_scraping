# Google Play Store Review Scraper

A Python-based tool that automates the process of scraping reviews from the Google Play Store using browser automation and AI-powered interactions.

## Features

- Automated navigation to Google Play Store app pages
- Dynamic review filtering by star rating
- Sorting reviews by date
- Simulated human-like scrolling behavior
- AI-powered browser interactions using LangChain and Gemini
- Asynchronous operation for better performance

## Prerequisites

- Python 3.8 or higher
- Google API key for Gemini AI
- Chrome browser installed

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/browser-use-scraping.git
cd browser-use-scraping
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the project root and add your Google API key:
```
api_key=your_gemini_api_key_here
```

## Usage

```python
from main import scrape_play_store_html
import asyncio

async def main():
    app_id = "com.example.app"  # Replace with your target app ID
    review = "2-star"          # Filter reviews by star rating
    result = await scrape_play_store_html(review, app_id)
    print(result)

asyncio.run(main())
```

## Configuration

You can customize the scraping behavior by modifying the following parameters in `main.py`:

- `scroll_timeout`: Duration of scrolling simulation (default: 120 seconds)
- `model`: Gemini AI model version (default: 'gemini-2.0-pro-exp-02-05')

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Disclaimer

This tool is for educational and research purposes only. Please ensure you comply with Google Play Store's terms of service and robots.txt when using this tool. 