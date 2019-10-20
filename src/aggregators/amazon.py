
import re
import requests
import string
import sys
from bs4 import BeautifulSoup

class AmazonAggregator:
    def __init__(self, data_file):
        self.data_file = data_file

        self.format_str = '[{0}] [{1}] [{2}] [{3}] [{4}] [{5}] [{6}]' #'[date] [product] [seller] [title] [stars] [message] [link]'

        self.url_regex = re.compile(r'^(?:https*:\/\/www.amazon.com\/)([^\/]+)\/[^\/]+\/([^\/]+).*$')
        self.review_page_regex = re.compile(r'^<.*>Showing\s[\d,]+-([\d,]+)\sof\s([\d,]+) reviews<\/.*>$')
        self.review_find_regex = re.compile(r'customer_review-\w+')
        self.review_title_regex = re.compile(r'<.+ href="(.*)"><[^>]+>(.*)<[\s\S]+')
        self.review_stars_regex = re.compile(r'<.+><.+>(\d)\.0 out of 5 stars<.+>')
        self.review_date_regex = re.compile(r'<[^>]+>([\w\d\s,]+).*')
        self.review_message_regex = re.compile(r'<[^>]+><[^>]+>(.*)<\/span>[\s\S]*')

        self.http_header = {'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1'}

    def get_from_url(self, url):
        r = requests.get(url,headers=self.http_header)
        if r.status_code != 200:
            raise Exception('HTTP Status Code: {0} Most likely malformed URL.'.format(r.status_code))
            return []

        soup = BeautifulSoup(r.text, 'lxml')
 
        product = str(soup.find(attrs={'id':'productTitle'}).string).strip(string.whitespace)
        seller = str(soup.find(attrs={'id':'bylineInfo'}).string).strip(string.whitespace)

        m = self.url_regex.match(url)
        g = m.groups()
        formatted_url = 'https://www.amazon.com/{0}/product-reviews/{1}'.format(g[0], g[1])
        url_params = {'ie':'UTF8', 'reviewerType':'all_reviews', 'pageNumber':1}

        review_data = []
        page_info = ['0', '1']
        
        while page_info[0] != page_info[1] and url_params['pageNumber'] <= 500:
            r = requests.get(formatted_url, params=url_params,headers=self.http_header)
            if r.status_code == 200:
                soup = BeautifulSoup(r.text, 'lxml')
                reviews = soup.find_all(attrs={'id':self.review_find_regex})
                for review in reviews:
                    review_soup = BeautifulSoup(str(review), 'lxml')
                    stars = self.review_stars_regex.match(str(review_soup.find(attrs={'data-hook':'review-star-rating'}))).group(1)
                    
                    title_data = self.review_title_regex.match(str(review_soup.find(attrs={'data-hook':'review-title'}))).groups()
                   
                    title = title_data[1]
                    link = 'https://www.amazon.com' + title_data[0]

                    date = self.review_date_regex.match(str(review_soup.find(attrs={'data-hook':'review-date'}))).group(1)

                    message = self.review_message_regex.match(str(review_soup.find(attrs={'data-hook':'review-body'}))).group(1)

                    review_data.append(self.format_str.format(date, product, seller, title, stars, message, link))

                f = str(soup.find(attrs={'data-hook':'cr-filter-info-review-count'}))
                
                page_info = self.review_page_regex.match(f).groups()
                url_params['pageNumber'] += 1
        
        return review_data

    def get_from_query(self, query):
        pass

    def log_data(self, data_str=None, data_list=None):
        if data_str:
            with open(self.data_file, mode='a', encoding='utf-8') as f:
                f.write(data_str)
                f.write('\n')
        elif data_list:
            with open(self.data_file, mode='a', encoding='utf-8') as f:
                for data in data_list:
                    f.write(data)
                    f.write('\n')
        else:
            raise Exception('No data strings or data lists provided to log.')
        