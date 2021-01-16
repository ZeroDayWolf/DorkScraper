import click
from selenium import webdriver
from dorkscraper import DorkScraper

web_driver = webdriver.Firefox()
scraper = DorkScraper(web_driver)

@click.command()
@click.argument('query')
def search(query):
    search = scraper.googleSearch(query)
    search_links = search["Links"]

    for link in search_links:
        print(link.get_attribute("href"))

if __name__ == "__main__":
    search()