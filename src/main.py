
import tkinter as tk

from aggregators.amazon import AmazonAggregator
#from aggregators.youtube import YoutubeAggregator

amazon_agg = AmazonAggregator('amazon_data.txt')

def main():
    w = tk.Tk()

    w.title('Review Scraper')
    tk.Label(w,text='Amazon Product URL').grid(row=0,column=0)
    url_entry = tk.Entry(w, width=100)
    url_entry.grid(row=0,column=1)
    status_label = tk.Label(w,text='')
    status_label.grid(row=1,column=0)
    tk.Button(w, text='Scrape Reviews', command=lambda status=status_label, url_e=url_entry: scrape(url_e, status)).grid(row=1,column=1)
    
    w.mainloop()

def scrape(url_entry, status_label):
    url = url_entry.get()
    data = []
    if url:
        try:
            status_label.config(text='Working...')
            data = amazon_agg.get_from_url(url)
        except Exception as e:
            print(e)
            status_label.config(text='Error making request.')
        else:
            try:
                amazon_agg.log_data(data_list=data)
            except Exception as e:
                print(e)
                status_label.config(text='Error writing review data.')
            else:
                status_label.config(text='Success!')
    else:
        status_label.config(text='Please enter a URL.')


if __name__ == '__main__':
    main()
