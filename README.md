# patriot-hacks-2019
Submission for Informed xp track of Patriot Hacks 2019.

The script has uses a simple user interface made in Tkinter that accepts an Amazon product URL and uses it to scrape customer review data about that product.

This project is written in python and the data produced is meant to be onboarded into Splunk to provide a searchable interface.

# Dependencies
This project depends on the following packages not included with python:
`requests` -- For making HTTP requests to collect HTML data from Amazon.
`beautifulsoup4` -- For parsing the collected HTML data.
`fake_useragent` -- So Amazon doesn't stop us from making automated requests (again) :)
