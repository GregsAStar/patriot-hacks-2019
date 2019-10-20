# patriot-hacks-2019
Submission for Informed xp track of Patriot Hacks 2019.

The script has uses a simple user interface made in Tkinter that accepts an Amazon product URL and uses it to scrape customer review data about that product.

This project is written in python and the data produced is meant to be onboarded into Splunk to provide a searchable interface.

We decided to undertake the task of creating a database that can easily record product listings and their reviews. In our demo we wrote a scraper to gather data from Amazon, however the process is applicable to other sources. The purpose of this product is to create a system where a user only needs to input a product listing in order to obtain user experience data from customer reviews.

# Structure
The `src` directory contains the source code for the web scraper.
The `media` directory contains screenshots of our work and a presentation about our solution.

# Dependencies
This project depends on the following packages not included with python:

`requests` -- For making HTTP requests to collect HTML data from Amazon.

`beautifulsoup4` -- For parsing the collected HTML data.

`fake_useragent` -- So Amazon doesn't stop us from making automated requests (again) :)
