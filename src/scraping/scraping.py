import requests
import re
from bs4 import BeautifulSoup
import csv
import os

class Scraping():
    def __init__(self, url, number, difficulty, language):
        self.url = url + number + '/tasks/abc' + number + '_'
        self.number = number
        self.difficulty = difficulty
        self.language = language

    def get_problem(self):
        response = requests.get(self.url + self.difficulty)
        soup = BeautifulSoup(response.text, 'html.parser')
        tag = soup.find_all(class_="lang")
        #print(tag)
        pro = tag[0].find_all(class_='lang-' + self.language)
        problem_list = []
        for part in pro[0].find_all(class_='part'):
            problem_list.append(part.text)

        problem_list = list(map(lambda x: x.replace('\r', ''), problem_list))
        problem_list = list(map(lambda x: x.replace('\\leq', '≦'), problem_list))
        problem_list = list(map(lambda x: x.replace('\\lt', '<'), problem_list))
        for i in ['問題文', '制約', '注釈', '出力']:
            problem_list = list(map(lambda x: x.replace(i, i + '\n'), problem_list))

        for i in ['入力入']:
            problem_list = list(map(lambda x: x.replace(i, i[0:2] + '\n' + i[2]), problem_list))

        for i in range(1, 5):
            problem_list = list(map(lambda x: x.replace('入力例 ' + str(i), '入力例 ' + str(i) + '\n'), problem_list))
            problem_list = list(map(lambda x: x.replace('出力\n例 ' + str(i), '出力例 ' + str(i) + '\n'), problem_list))

        problem_list = list(map(lambda x: x.replace('\n\n\n', '\n\n'), problem_list))
        problem_list = list(map(lambda x: x.replace('\n\n', '\n'), problem_list))
        
        #print(problem_list)
        return problem_list

    def write_problem(self, l):
        with open('../../data/' + self.language + '/problems' + self.number + '_' + self.difficulty + '.txt', 'w', encoding='utf-8') as f:
            f.writelines(l)
    


if __name__ == '__main__':
    url = 'https://atcoder.jp/contests/abc'
    scraping = Scraping(url, '212', 'a', 'ja')
    problem = scraping.get_problem()
    scraping.write_problem(problem)
    
    