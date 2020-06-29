# DorkScraper v 0.2
## Description
Dorkscraper is a tool for **Google Dork Hacking.** All Google dorks in this tool can be found in the **GHDB**.
The creator is not responsible for any misuse of this tool. Please use legally.
## Dependecies
*Python 3
*Selenium
*Selenium Firefox Webdriver
## Usage
`python dorkscraper.py <dork> <output_mode> <tld>`
Tld is the top level domain or target site you wish to dork. Example: .gov or walmart.com
## Output Modes
* -t
 ** This will print all of the information, in an unclean format.
 ** URLS and Descriptions. 
* -c
 ** This will format the scraped information cleanly.
 ** The URLS will be output in this format: url.com > route > file > ext
 ** The > mean / or . Here the unformatted url would be:  url.com/route/file.ext
## Available Dorks
* -fp for password files.
* -av for advisories and vulnerabilities.
* -ws for web servers.
* -vs for vulnerable servers
* -lp for login portals
* -fh for footholds.
* -vo for various online devices.
* -cam for online cameras.
* -ji for juicy information.
* -si for sensitive shopping info.
