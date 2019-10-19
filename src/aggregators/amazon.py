
import requests


class AmazonAggregator:
    def __init__(self):
        self.format_str = f''

    def get_from_url(self, url):
        pass

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
        