# amazon-web-scraper



This repository contains a Scrapy project to scrape information about iPhones listed on website. The scraper extracts details such as the product name, price, rating, and number of reviews.

## Table of Contents

- Installation
- Usage
- Project Structure


## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/RohitPawar001/amazon-web-scraper.git
    cd amazon
    ```

2. Use scrapeops api
 <br>
     Add the your scrapeops aip key  and user agents url in settings.py file <br>
     Add your user agents and browser header url from scrapeops into the middlewares.py file

4. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

5. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Navigate to the project directory:
    ```bash
    cd amazon
    ```

2. Run the Scrapy spider:
    ```bash
    scrapy crawl mobile -o smartphones.csv
    ```

   This will start the spider and save the scraped data to `smartphones.csv`.

## Project Resources

<br>
python :- https://www.python.org/downloads/
<br>
scrapy :- https://scrapy.org/

## Scrapeops 
  scrapeops is used to attach the fake user agents and fake browser headers for not getting blocked by website https://scrapeops.io/



