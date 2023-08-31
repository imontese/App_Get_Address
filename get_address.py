import sys
import os
import numpy as np 
import pandas as pd
from datetime import date, datetime
import re
import time
import csv

from bs4 import BeautifulSoup as soup
from urllib.request import Request, urlopen
import requests
from requests_html import HTMLSession
import warnings
warnings.filterwarnings('ignore')

class etherscan_file():
    def __init__(self, mode_box, min_amount, num_address):
        # read cvs file from etherscan and get the addresses with highest token transaction 
        self.df = pd.read_csv("ERC20Data/address.csv")
        self.df_time = pd.read_csv("ERC20Data/address_time.csv", header=None)
        self.df = self.df[['DateTime', 'To', 'Quantity']]

        # convert Quantity column to float
        self.df['Quantity'] = self.df['Quantity'].apply(lambda x: float(x.replace(",", ""))).round(2)
        # drop duplicate addresses and keep the one with the highest value
        self.df = self.df.sort_values(['To', 'Quantity'], ascending=[True, False]).drop_duplicates(['To'], keep='first')
        self.df = self.df.sort_values('Quantity', ascending=False)
        self.address = self.df['To'][0:num_address]

        # add time at the beginning of each request
        now = datetime.now().replace(microsecond=0)
        with open('greater_address.txt', 'a') as f:
            f.write('-------NEW-------' + str(now) + '-------' '\n')

        with open('greater_address.csv', 'a', newline='') as f:
            writer = csv.writer(f, delimiter=',')
            writer.writerow(['-------NEW-------', str(now)])

        if mode_box == 'Only date':
            for add in self.df_time[0]:
                self.last_tx(add)
        elif mode_box == 'Address with date':
            for add in self.address:
                self.address_amount(add, min_amount)
                
    # if the amount holds in the address is greater than the hold the address will be saved in the txt file
    def address_amount(self, add, hold):
        # creating the url
        pre = 'https://etherscan.io/address/'
        suf = '#tokentxns'
        url = pre + add + suf
        req = Request(url, headers = {'User-Agent':'Mozilla/5.0'})
        webpage = urlopen(req)
        page_soup = soup(webpage, 'html.parser')

        #extract the part to be used
        contents = page_soup.main
        button = contents.find_all('button', attrs={'class': 'js-dropdowns-input-focus btn btn-white text-start w-100 dropdown-toggle py-2 px-3'})
        
        # scraping last transaction
        pre = 'https://etherscan.io/address-tokenpage?m=l&a='
        url = pre + add
        req = requests.get(url, headers = {'User-Agent':'Mozilla/5.0'}, timeout=5)
        page_soup = soup(req.text, 'html.parser')
        pag_lastTx = page_soup.find('td', attrs={'class': 'showAge'})

        try:
            first_stream = button[0]
            match = re.search(r'\$[0-9,.]*', first_stream.text)
            if match:
                total = match.group()
                amount = float(total.replace("$", "").replace(",", ""))
                if amount > hold:
                    # with open('greater_address.txt', 'a') as f:
                        
                    #     f.write(add + '\t' + total + '\t' + address_date +'\n')

                    link = 'https://etherscan.io/address/' + add + '#tokentxns'
                    address_date = pag_lastTx.text
                    with open('greater_address.csv', 'a', newline='') as f:
                        writer = csv.writer(f, delimiter=',')
                        writer.writerow([add, total, address_date, '=hyperlink("'+link+'","Link")'])
                        # find the last transaction part
        except:
            pass

        time.sleep(1)
    

    def last_tx(self, add):
        # creating the url
        pre = 'https://etherscan.io/address-tokenpage?m=l&a='
        url = pre + add
        req = requests.get(url, headers = {'User-Agent':'Mozilla/5.0'}, timeout=5)
        # webpage = urlopen(req)
        page_soup = soup(req.text, 'html.parser')

        
        try:
            #extract the part to use
            # contents = page_soup.main
            pag_lastTx = page_soup.find('td', attrs={'class': 'showAge'})
            time_sec = pag_lastTx.text

            d = re.search(r'(days|day)', time_sec)
            h = re.search(r'(hrs|hr)', time_sec)
            m = re.search(r'(mins|min)', time_sec)
            self.days, self.hrs, self.mins = 0,0,0
            
            #getting the right date depending on the format 
        
            if d != None:
                days = re.search(r'[0-9]*', time_sec).group()
                if h != None:
                    self.hrs = re.search(r'[0-9]+', time_sec[d.span()[1]+1:]).group()
            elif h != None:
                self.hrs = re.search(r'[0-9]+', time_sec).group()
                if m != None:
                    self.mins = re.search(r'[0-9]+', time_sec[h.span()[1]+1:]).group()
            elif m != None:
                    self.mins = re.search(r'[0-9]+', time_sec).group()

            # print('D ' + str(self.days) + " H " + str(self.hrs) + " M " + str(self.mins))
            # Link
            link = 'https://etherscan.io/address/' + add + '#tokentxns'
            address_date = pag_lastTx.text
            with open('greater_address.csv', 'a', newline='') as f:
                writer = csv.writer(f, delimiter=',')
                writer.writerow([add, '', address_date, '=hyperlink("'+link+'","Link")'])
                # f.write(add + '\t' + address_date +'\n')
        
        except:
            pass

        time.sleep(1)
