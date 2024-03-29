<h1>Radio Data Scraper</h1>

This Python script scrapes radio station data from a website and saves it to a CSV file. It utilizes BeautifulSoup for web scraping and requests for making HTTP requests.
Installation

Clone the repository to your local machine:

```
bash

git clone <repository_url>
```
Navigate to the project directory:

```
bash

cd radio-data-scraper
```

Install the required dependencies:
```
pip install -r requirements.txt
```

<h2>Usage</h2>

    Modify the base_url variable in the script to point to the desired website.
    Run the script:

<h2>python radio_scraper.py</h2>

    The script will scrape the radio station data and save it to a CSV file named radio_data.csv in the current directory.

<h2>Explanation</h2>

    The script starts by defining the base URL of the website to scrape and the page number.
    It then opens a CSV file in write mode and writes the headers.
    Inside a while loop, it constructs the URL for each page, retrieves the page source using requests, and parses it using BeautifulSoup.
    It extracts relevant information such as radio station name, country, genres, frequencies, and website URL from the HTML using BeautifulSoup's methods.
    The extracted data is then written to the CSV file row by row.
    The loop continues until there are no more pages to scrape.

<h2>Dependencies</h2>

    requests: HTTP library for making requests and working with responses.
    Beautiful Soup: Python library for pulling data out of HTML and XML files.

<h2>Contributing</h2>

Contributions are welcome! If you have any suggestions, improvements, or feature requests, please open an issue or submit a pull request.
