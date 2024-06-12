#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Filename :Shiranui Kai Ni
@Description :This is a Web Crawler to get Exchange Rate data from CNY to USD, then use it to calculate the USD amount of original CNY amount.
@Datatime :2020/12/14 15:46:52
@Author :Secary
@Version :v1.0
'''

import bs4                              
import re                               
import urllib.request,urllib.error,urllib.parse      
import xlwt                             #
from bs4 import BeautifulSoup
import datetime
import time
from datetime import datetime,date,timedelta

findExchangeRate = re.compile(r'<div>1美元 ≈ (.*?)人民币</div>')

def main():
    url = "https://www.baidu.com/s?ie=UTF-8&wd=%E4%BA%BA%E6%B0%91%E5%B8%81%E5%AF%B9%E7%BE%8E%E5%85%83"
    CnyToUsdExchange = getData(url)
    CurrentTime = time.strftime('%Y-%m-%d %H:%m:%S', time.localtime(time.time()))
    print("%s\nToday's Exchange Rate of CNY to USD is %s "%(CurrentTime,CnyToUsdExchange[0][0]))
    Exchange_rate = float(CnyToUsdExchange[0][0])
    try:
        print('-'*20,'CNY To USD','-'*20)
        while 1:
            try: 
                CNY = input("CNY:")
                if CNY != "esc":
                    USD = float(CNY)/Exchange_rate
                    print("USD:%s"%USD)
                    print('=' * 52)
                else:
                    break    
            except Exception as report:
                print(report)
                print('=' * 52)
    except Exception as  result:
        print("ERROR:%s"%result)

def askurl(url):
    head = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36'
    }
    request = urllib.request.Request(url,headers=head)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode('utf-8')
    except urllib.error.HTTPError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reson"):
            print(e.reason)
    return html

def getData(url):
    html = askurl(url)
    soup = BeautifulSoup(html,"html.parser")
    for item in soup.find_all('div', class_="op_exrate_result"):
        item = str(item)
        Exchange = []
        ExchangeToday = re.findall(findExchangeRate,item)
        Exchange.append(ExchangeToday)
    return Exchange

if __name__ == "__main__":
    main()
