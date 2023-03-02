import requests
import re
from bs4 import BeautifulSoup
import csv
import os

class Scraping():
    def __init__(self, url, number, difficulty, language):
        
        if number < 10:
            self.number = '00' + str(number)
        elif number < 100:
            self.number = '0' + str(number)
        else:
            self.number = str(number)
        
        if 0 < number < 20:
            if difficulty == 'a':
                self.difficulty = '1'
            elif difficulty == 'b':
                self.difficulty = '2'
            elif difficulty == 'c':
                self.difficulty = '3'
            else:
                self.difficulty = '4'
        else:
            self.difficulty = difficulty
        
        self.language = language

        self.url = url + self.number + '/tasks/abc' + self.number + '_'
    
    # 42~
    # ? ~ 57のc,dはabcではなくarc　だいたい　問題番号 + 14
    # 58~のc,dはちょくちょくabcではなくagc
    def get_problem(self):
        response = requests.get(self.url + self.difficulty)
        soup = BeautifulSoup(response.text, 'html.parser')
        tag = soup.find_all(class_="lang")
        if len(tag) == 0:
            return []
        #print(tag)
        pro = tag[0].find_all(class_='lang-' + self.language)
        problem_list = []
        for part in pro[0].find_all(class_='part'):
            problem_list.append(part.text)

        problem_list = list(map(lambda x: x.replace('\r', ''), problem_list))
        problem_list = list(map(lambda x: x.replace('\\leq', '≦'), problem_list))
        problem_list = list(map(lambda x: x.replace('\\lt', '<'), problem_list))
        problem_list = list(map(lambda x: x.replace('\\', ''), problem_list))

        if self.language == 'ja':
            for i in ['問題文', '制約', '注釈', '出力']:
                problem_list = list(map(lambda x: x.replace(i, i + '\n'), problem_list))

            for i in ['入力入']:
                problem_list = list(map(lambda x: x.replace(i, i[0:2] + '\n' + i[2]), problem_list))

            for i in range(1, 5):
                problem_list = list(map(lambda x: x.replace('入力例 ' + str(i), '入力例 ' + str(i) + '\n'), problem_list))
                problem_list = list(map(lambda x: x.replace('出力\n例 ' + str(i), '出力例 ' + str(i) + '\n'), problem_list))

        else:
            for i in ['Problem Statement', 'Constraints', 'Notes', 'Output']:
                problem_list = list(map(lambda x: x.replace(i, i + '\n'), problem_list))

            for i in ['InputInput']:
                problem_list = list(map(lambda x: x.replace(i, i[0:5] + '\n' + i[5:]), problem_list))

            for i in range(1, 5):
                problem_list = list(map(lambda x: x.replace('Sample Input ' + str(i), 'Sample Input ' + str(i) + '\n'), problem_list))
                problem_list = list(map(lambda x: x.replace('Sample Output\n ' + str(i), 'Sample Output ' + str(i) + '\n'), problem_list))

        problem_list = list(map(lambda x: x.replace('\n\n\n', '\n\n'), problem_list))
        problem_list = list(map(lambda x: x.replace('\n\n', '\n'), problem_list))
        #print(problem_list)
        return problem_list

    def write_problem(self, l):
        if len(l) != 0:
            with open('../../data/' + self.language + '/problems' + self.number + '_' + self.difficulty + '.txt', 'w', encoding='utf-8') as f:
                f.writelines(l)
        else:
            with open('../../data/errors.txt', 'a') as f:
                f.write(self.number + '-' + self.difficulty + '-' + self.language + '\n')

if __name__ == '__main__':
    if os.path.exists('../../data/errors.txt'):
        os.remove('../../data/errors.txt')
    url = 'https://atcoder.jp/contests/abc'
    '''
    scraping = Scraping(url, 42, 'c', 'ja')
    problem = scraping.get_problem()
    scraping.write_problem(problem)
    scraping = Scraping(url, 42, 'c', 'en')
    problem = scraping.get_problem()
    scraping.write_problem(problem)
    '''
    for number_of_problem in range(42, 70):
        for difficulty in ['a', 'b', 'c', 'd']:
            scraping = Scraping(url, number_of_problem, difficulty, 'ja')
            problem = scraping.get_problem()
            scraping.write_problem(problem)
            scraping = Scraping(url, number_of_problem, difficulty, 'en')
            problem = scraping.get_problem()
            scraping.write_problem(problem)
        print(number_of_problem)

    