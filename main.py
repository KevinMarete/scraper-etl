import bonobo
import os

from config import OUTPUT_FILE
from scraper import ZillowScraper, RedfinScraper


def extract():
    yield ZillowScraper('https://www.zillow.com/homes/8-Mallard-Ave,-Boston,-MA-02124_rb/59106911_zpid/').run()
    yield RedfinScraper('https://www.redfin.com/MA/Boston/8-Mallard-Ave-02124/home/9072531').run()


def transform(source: str, price: str):
    t_price = price.replace(',', '').lstrip('$')
    return source, t_price


def load(source: str, price: str):
    with open(OUTPUT_FILE, 'a+', encoding='utf8') as f:
        f.write((source + ' : ' + price + '\n'))


if __name__ == '__main__':
    # Remove output file
    if os.path.isfile(OUTPUT_FILE):
        os.unlink(OUTPUT_FILE)

    graph = bonobo.Graph(
        extract,
        transform,
        load,
    )
    bonobo.run(graph)
