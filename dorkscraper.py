from time import sleep
import requests

class DorkScraper():
    def __init__(self, webdriver, tld=None):
        self.webdriver = webdriver
        self.tld = tld

    # Googles a singular query and returns the result.
    def googleSearch(self, query):

        result = {}
        self.webdriver.get("https://google.com/search?q="+query)

        links = self.webdriver.find_elements_by_xpath("//a[@href]")
        divs  = self.webdriver.find_elements_by_tag_name("div")
        paragraphs = self.webdriver.find_elements_by_tag_name("p")

        result["Links"] = links
        result["Divs"] = divs
        result["Paragraphs"] = paragraphs

        return result

    #Googles a list of queries.
    def googleQueries(self, queries):
        result = []
        for query in queries:
            search_result = self.googleSearch(query)
            result.append(search_result)
        return result