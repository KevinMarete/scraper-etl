# SCRAPER_ETL

Scraper ETL uses Bonobo. It scraps Zillow and Redfin for Property Listing Prices.

---

## Requirements

For development, you will only need Python 3.5+ and a python global package such as pip, installed in your environment. Follow this guide on [Medium](https://medium.com/python-pandemonium/develop-your-first-etl-job-in-python-using-bonobo-eaea63cc2d3c).

## Install

    $ git clone https://github.com/KevinMarete/scraper-etl
    $ cd scraper-etl
    $ python3 -m venv bonono-venv
    $ . bonobo-venv/bin/activate
    $ pip install -r requirements.txt

## Running the Bonobo ETL

    $ bonobo run main.py