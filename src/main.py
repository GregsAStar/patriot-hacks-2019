
import sys

from aggregators.amazon import AmazonAggregator
#from aggregators.youtube import YoutubeAggregator


def main():
    amazon_agg = AmazonAggregator('amazon_data.txt')
    data = amazon_agg.get_from_url(input())
    for datum in data:
        print(datum, '\n\n')
    amazon_agg.log_data(data_list=data)

if __name__ == '__main__':
    main()
