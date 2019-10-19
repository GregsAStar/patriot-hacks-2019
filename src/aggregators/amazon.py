
import requests
import re
from bs4 import BeautifulSoup

class AmazonAggregator:
    def __init__(self):
        self.format_str = '[{0}] [{1}] [{2}] [{3}]' #'[title] [stars] [message] [link]'
        self.url_regex = re.compile(r'^(?:https*:\/\/www.amazon.com\/)(?<name>[^\/]+)\/[^\/]+\/(?<id>[^\/]+).*$')
        self.review_page_regex = re.compile(r'^<.*>Showing\s\d+-(\d+)\sof\s(\d+) reviews<\/.*>$')
        self.review_find_regex = re.compile(r'id=customer_review-\w+')
        self.review_title_regex = re.compile(r'')

    def get_from_url(self, url):
        m = self.url_regex.match(url)
        g = m.group
        formatted_url = 'https://www.amazon.com/{0}/product-reviews/{1}'.format(g('name'), g('id'))
        url_params = {'ie':'UTF8', 'reviewerType':'all_reviews', 'pageNumber':1}
    
        page_info = ['0', '1']
        while page_info[0] != page_info[1]:
            r = requests.get(formatted_url, params=url_params)
            if r.status_code == 200:
                soup = BeautifulSoup(r.text, 'html_parser')
                reviews = soup.find_all(review_find_regex)
                for review in reviews:
                    review.find(review_title_regex)
                f = soup.find(attrs={'data-hook':'cr-filter-info-review-count'})
                page_info = self.review_page_regex.match(f).groups
                url_params['pageNumber'] += 1




    def get_from_query(self, query):
        pass

    def log_data(self, data_str=None, data_list=None):
        if data_str:
            with open('amazon_data.txt', 'a') as f:
                f.write(data_str)
        elif data_list:
            with open('amazon_data.txt', 'a') as f:
                for data in data_list:
                    f.write(data)
        else:
            raise Exception('No data strings or data lists provided to log.')
        