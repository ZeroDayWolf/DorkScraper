from dorkscraper import DorkScraper
from selenium import webdriver

web_driver = webdriver.Firefox()


scraper = DorkScraper(web_driver)

search = scraper.googleSearch('intext:Basato su IceWarp Server')

search_links = search["Links"]

for link in search_links:
    print(link.get_attribute("href"))