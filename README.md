[![made-with-python3](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![Python 3.7](https://img.shields.io/badge/python-3.7-blue.svg)](https://www.python.org/downloads/release/python-360/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Version: 0.3]]

## Description

Dorkscraper is a tool for **Google Dork Hacking.** All Google dorks in this tool can be found in the **GHDB**.
The creator is not responsible for any misuse of this tool. Please use legally.

## Dependecies

* Python 3
* Selenium
* Selenium Webdriver of choice. (Works best with firefox geckodriver, the CLI supports **only** Firefox.)
* click command line interface creation kit.

## Usage

DorkScraper comes with two main files both with different uses, the first file dorkscraper.py is a Python module. The second file dorkscrapercli.py is the CLI for DorkScraper.

### Using DorkScraper as a module

The following example can be found in example.py

```python
from dorkscraper import DorkScraper
from selenium import webdriver

web_driver = webdriver.Firefox()


scraper = DorkScraper(web_driver)

mySearch = scraper.googleSearch('intext:Basato su IceWarp Server')

searchLinks = mySearch["Links"]

for link in searchLinks:
    print(link.get_attribute("href"))
```
This example will print out all links\URLs it finds on the page.

### Using DorkScraper CLI.

The DorkScraper CLI 


## Available Dorks

* -pf for password files.
* -av for advisories and vulnerabilities.
* -ws for web servers.
* -vs for vulnerable servers
* -lp for login portals
* -fh for footholds.
* -vo for various online devices.
* -cam for online cameras.
* -ji for juicy information.
* -si for sensitive shopping info.
