#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Filename :Amakaze
@Description :This is a Web Crawler to get Exchange Rate data from CNY to AUD
@Datatime :2024/06/13
@Author :Secary
@Version :v1.0
'''

import bs4                              
import re                               
import urllib.request,urllib.error,urllib.parse                            #
from bs4 import BeautifulSoup
import datetime
import time
from datetime import datetime,date,timedelta

website = "https://www.boc.cn/sourcedb/whpj/"

def askurl(url):
    head = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36'
    }
    request = urllib.request.Request(url,headers=head)
    html = ""
    try:
        # time.sleep(5)
        response = urllib.request.urlopen(request)
        html = response.read().decode('utf-8')
    except urllib.error.HTTPError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reson"):
            print(e.reason)
    return html

def askurl(url):
    head = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36'
    }
    request = urllib.request.Request(url,headers=head)
    html = ""
    try:
        # time.sleep(5)
        response = urllib.request.urlopen(request)
        html = response.read().decode('utf-8')
    except urllib.error.HTTPError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reson"):
            print(e.reason)
    return html

def getexchange_rate(url):
    html = askurl(url)
    soup = BeautifulSoup(html,"html.parser")
    target_td = soup.find('td', text='澳大利亚元')
    if target_td:
        next_td = target_td.find_next_sibling('td')
        if next_td:
            result = float(next_td.text.strip())
        else:
            result = "未找到相邻的<td>标签"
    else:
        result = "未找到包含'澳大利亚元'的<td>标签"
        
    return result

def main(url):
    cn_aud = getexchange_rate(url)
    if type(cn_aud) == float:
        CurrentTime = time.strftime('%Y-%m-%d %H:%m:%S', time.localtime(time.time()))
        print("%s\nToday's Exchange Rate of CNY to AUD is %s "%(CurrentTime,cn_aud))
        Exchange_rate = float(cn_aud)
    else:
        Exchange_rate = "抓取汇率失败，原因：" +  cn_aud
        
    return Exchange_rate

if __name__ == "__main__":
    main(website)
    

    

