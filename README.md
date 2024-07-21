# amazon-web-scraper



This repository contains a Scrapy project to scrape information about iPhones listed on Amazon. The scraper extracts details such as the product name, price, rating, and number of reviews.

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

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required dependencies:
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
website :-  https://www.amazon.in/s?bbn=1389401031&rh=n%3A1389401031%2Cp_89%3AApple&dc&qid=1717581794&rnid=3837712031&ref=lp_1389401031_nr_p_89_0
<br>
python :- https://www.python.org/downloads/
<br>
scrapy :- https://scrapy.org/

## Scrapeops 
  scrapeops is used to attach the fake user agents and fake browser headers for not getting blocked by amazon https://scrapeops.io/



