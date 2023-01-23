import requests
import re
from bs4 import BeautifulSoup
import csv
import os

class Scraping():
    def __init__(self, url, number):
        self.url = url
        self.number = number

    def get_problem(self):
        response = requests.get(self.url)
        soup = BeautifulSoup(response.content, 'html.parser')
        print(soup)
        #problem = soup.find_all(href=re.compile("https://atcoder.jp/contests/abc" + self.number + "/tasks/abc" + self.number + "_"))
        #problem = soup.find(href=re.compile("https://atcoder.jp/contests/abc285/tasks/abc285_a"))
        #problem = soup.find_all(id='root')
        #return problem.find
        tag = soup.find(id="event-overview")
        print(tag)

if __name__ == '__main__':
    url = 'https://kenkoooo.com/atcoder/#/table/'
    #url = 'https://conf.researchr.org/track/icse-2021/icse-2021-papers?#event-overview'
    scraping = Scraping(url, '285')
    problem = scraping.get_problem()
    #print(problem)
