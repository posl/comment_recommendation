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
        #self.add_number = add_number
        self.url = url + self.number + '/tasks/abc' + self.number + '_'
    
    # 42~
    # 42 ~ 50のc,dはabcではなくarc　だいたい　問題番号 + 16 + a,b
    # 52 ~ 53のc,dはabcではなくarc　だいたい　問題番号 + 15 + a,b
    # 55 ~ 56のc,dはabcではなくarc　だいたい　問題番号 + 14 + a,b 
    # 58 ~ 60　は　　+ 13

    def get_problem(self):
        #print(self.url + self.difficulty)
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
        problem_list = list(map(lambda x: x.replace('\\geq', '≧'), problem_list))
        problem_list = list(map(lambda x: x.replace('\\lt', '<'), problem_list))
        problem_list = list(map(lambda x: x.replace('\\gt', '>'), problem_list))
        problem_list = list(map(lambda x: x.replace('\\neq', '≠'), problem_list))
        problem_list = list(map(lambda x: x.replace('\\ldots', '...'), problem_list))
        problem_list = list(map(lambda x: x.replace('\\dots', '...'), problem_list))
        problem_list = list(map(lambda x: x.replace('{,}', ''), problem_list))
        #print(problem_list)
        problem_list = list(map(lambda x: x.replace('\\,', ''), problem_list))
        problem_list = list(map(lambda x: x.replace('\\', ''), problem_list))
        problem_list = list(re.sub(r'{rm\s(\w+)}', r'\1', i) for i in problem_list)
        problem_list = list(re.sub(r'text{(\w+)}', r'\1', i) for i in problem_list)

        if self.language == 'ja':
            for i in ['問題文', '制約', '注釈', '出力']:
                problem_list = list(map(lambda x: x.replace(i, i + '\n'), problem_list))

            for i in ['入力入']:
                problem_list = list(map(lambda x: x.replace(i, i[0:2] + '\n' + i[2]), problem_list))

            for i in range(1, 6):
                problem_list = list(map(lambda x: x.replace('入力例 ' + str(i), '入力例 ' + str(i) + '\n'), problem_list))
                problem_list = list(map(lambda x: x.replace('出力\n例 ' + str(i), '出力例 ' + str(i) + '\n'), problem_list))

        else:
            for i in ['Problem Statement', 'Constraints', 'Notes', 'Output']:
                problem_list = list(map(lambda x: x.replace(i, i + '\n'), problem_list))

            for i in ['InputThe']:
                problem_list = list(map(lambda x: x.replace(i, i[0:5] + '\n' + i[5:]), problem_list))

            for i in range(1, 6):
                problem_list = list(map(lambda x: x.replace('Sample Input ' + str(i), 'Sample Input ' + str(i) + '\n'), problem_list))
                problem_list = list(map(lambda x: x.replace('Sample Output\n ' + str(i), 'Sample Output ' + str(i) + '\n'), problem_list))

        problem_list = list(map(lambda x: x.replace('\n\n\n', '\n\n'), problem_list))
        problem_list = list(map(lambda x: x.replace('\n\n', '\n'), problem_list))

        for i in ['出力\nせよ']:
            problem_list = list(map(lambda x: x.replace(i, '出力せよ'), problem_list))
        
        for i in ['出力\nして']:
            problem_list = list(map(lambda x: x.replace(i, '出力して'), problem_list))

        '''
        制約\n」, 出力\nは, 出力\nします, 問題文\nの, 問題文\n中, 出力\nの, 出力\nする
        '''
        problem_list[0] = problem_list[0].lstrip()
        #print(problem_list)
        return problem_list

    def write_problem(self, l):
        if len(l) != 0:
            with open('../../data/' + self.language + '/problems' + self.number + '_' + self.difficulty + '.txt', 'w', encoding='utf-8') as f:
                f.writelines(l)
        else:
            with open('../../data/errors.txt', 'a') as f:
                f.write(self.number + '-' + self.difficulty + '-' + self.language + '\n')
    
    def change_url(self, add_number):
        new_number = int(self.number) + add_number
        self.url = url + self.number + '/tasks/arc'

        if new_number < 100:
            new_number = '0' + str(new_number)
            self.url = self.url + str(new_number) + '_'
        
        else:
            self.url = self.url + str(new_number) + '_'

    def change_difficulty(self):
        if self.difficulty == 'a':
            self.difficulty = 'c'
        else:
            self.difficulty = 'd'
        
def change_add(number, add_number):
    number = number - add_number
    return number

if __name__ == '__main__':
    if os.path.exists('../../data/errors.txt'):
        os.remove('../../data/errors.txt')
    url = 'https://atcoder.jp/contests/abc'
    add_id = 16

    '''
    for number_of_problem in range(1, 42):
        for difficulty in ['a', 'b', 'c', 'd']:
            scraping = Scraping(url, number_of_problem, difficulty, 'ja')
            problem = scraping.get_problem()
            scraping.write_problem(problem)
            scraping = Scraping(url, number_of_problem, difficulty, 'en')
            problem = scraping.get_problem()
            scraping.write_problem(problem)
        print(number_of_problem)
    '''

    
    '''
    for number_of_problem in range(42, 51):
    #for number_of_problem in range(44, 45):
        for difficulty in ['a', 'b']:
            scraping = Scraping(url, number_of_problem, difficulty, 'ja')
            problem = scraping.get_problem()
            scraping.write_problem(problem)
            scraping = Scraping(url, number_of_problem, difficulty, 'en')
            problem = scraping.get_problem()
            scraping.write_problem(problem)

        # 実際はc,d
        for difficulty in ['a', 'b']:
            scraping = Scraping(url, number_of_problem, difficulty, 'ja')
            problem = scraping.get_problem()
            scraping.change_url(add_id)
            problem = scraping.get_problem()
            scraping.change_difficulty()
            scraping.write_problem(problem)
            scraping = Scraping(url, number_of_problem, difficulty, 'en')
            problem = scraping.get_problem()
            scraping.change_url(add_id)
            problem = scraping.get_problem()
            scraping.change_difficulty()
            scraping.write_problem(problem)
        print(number_of_problem)
    
    for number_of_problem in range(51, 52):
        for difficulty in ['a', 'b', 'c', 'd']:
            scraping = Scraping(url, number_of_problem, difficulty, 'ja')
            problem = scraping.get_problem()
            scraping.write_problem(problem)
            scraping = Scraping(url, number_of_problem, difficulty, 'en')
            problem = scraping.get_problem()
            scraping.write_problem(problem)
        print(number_of_problem)
    '''
    # 16 -> 15
    add_id = 15
    #for number_of_problem in range(52, 54):
    for number_of_problem in range(53, 54):
        for difficulty in ['a', 'b']:
            scraping = Scraping(url, number_of_problem, difficulty, 'ja')
            problem = scraping.get_problem()
            scraping.write_problem(problem)
            scraping = Scraping(url, number_of_problem, difficulty, 'en')
            problem = scraping.get_problem()
            scraping.write_problem(problem)

        # 実際はc,d
        for difficulty in ['a', 'b']:
            scraping = Scraping(url, number_of_problem, difficulty, 'ja')
            problem = scraping.get_problem()
            scraping.change_url(add_id)
            problem = scraping.get_problem()
            scraping.change_difficulty()
            scraping.write_problem(problem)
            scraping = Scraping(url, number_of_problem, difficulty, 'en')
            problem = scraping.get_problem()
            scraping.change_url(add_id)
            problem = scraping.get_problem()
            scraping.change_difficulty()
            scraping.write_problem(problem)
        print(number_of_problem)
    '''
    for number_of_problem in range(54, 55):
        for difficulty in ['a', 'b', 'c', 'd']:
            scraping = Scraping(url, number_of_problem, difficulty, 'ja')
            problem = scraping.get_problem()
            scraping.write_problem(problem)
            scraping = Scraping(url, number_of_problem, difficulty, 'en')
            problem = scraping.get_problem()
            scraping.write_problem(problem)
        print(number_of_problem)

    # 15 -> 14
    add_id = 14
    for number_of_problem in range(55, 57):
        for difficulty in ['a', 'b']:
            scraping = Scraping(url, number_of_problem, difficulty, 'ja')
            problem = scraping.get_problem()
            scraping.write_problem(problem)
            scraping = Scraping(url, number_of_problem, difficulty, 'en')
            problem = scraping.get_problem()
            scraping.write_problem(problem)

        # 実際はc,d
        for difficulty in ['a', 'b']:
            scraping = Scraping(url, number_of_problem, difficulty, 'ja')
            problem = scraping.get_problem()
            scraping.change_url(add_id)
            problem = scraping.get_problem()
            scraping.change_difficulty()
            scraping.write_problem(problem)
            scraping = Scraping(url, number_of_problem, difficulty, 'en')
            problem = scraping.get_problem()
            scraping.change_url(add_id)
            problem = scraping.get_problem()
            scraping.change_difficulty()
            scraping.write_problem(problem)
        print(number_of_problem)
    
    for number_of_problem in range(57, 58):
        for difficulty in ['a', 'b', 'c', 'd']:
            scraping = Scraping(url, number_of_problem, difficulty, 'ja')
            problem = scraping.get_problem()
            scraping.write_problem(problem)
            scraping = Scraping(url, number_of_problem, difficulty, 'en')
            problem = scraping.get_problem()
            scraping.write_problem(problem)
        print(number_of_problem)

    # 14 -> 13
    add_id = change_add(add_id, 1)
    for number_of_problem in range(58, 61):
        for difficulty in ['a', 'b']:
            scraping = Scraping(url, number_of_problem, difficulty, 'ja')
            problem = scraping.get_problem()
            scraping.write_problem(problem)
            scraping = Scraping(url, number_of_problem, difficulty, 'en')
            problem = scraping.get_problem()
            scraping.write_problem(problem)

        # 実際はc,d
        for difficulty in ['a', 'b']:
            scraping = Scraping(url, number_of_problem, difficulty, 'ja')
            problem = scraping.get_problem()
            scraping.change_url(add_id)
            problem = scraping.get_problem()
            scraping.change_difficulty()
            scraping.write_problem(problem)
            scraping = Scraping(url, number_of_problem, difficulty, 'en')
            problem = scraping.get_problem()
            scraping.change_url(add_id)
            problem = scraping.get_problem()
            scraping.change_difficulty()
            scraping.write_problem(problem)
        print(number_of_problem)
    
    for number_of_problem in range(61, 62):
        for difficulty in ['a', 'b', 'c', 'd']:
            scraping = Scraping(url, number_of_problem, difficulty, 'ja')
            problem = scraping.get_problem()
            scraping.write_problem(problem)
            scraping = Scraping(url, number_of_problem, difficulty, 'en')
            problem = scraping.get_problem()
            scraping.write_problem(problem)
        print(number_of_problem)

    # 13 -> 12
    add_id = change_add(add_id, 1)
    for number_of_problem in range(62, 64):
        for difficulty in ['a', 'b']:
            scraping = Scraping(url, number_of_problem, difficulty, 'ja')
            problem = scraping.get_problem()
            scraping.write_problem(problem)
            scraping = Scraping(url, number_of_problem, difficulty, 'en')
            problem = scraping.get_problem()
            scraping.write_problem(problem)

        # 実際はc,d
        for difficulty in ['a', 'b']:
            scraping = Scraping(url, number_of_problem, difficulty, 'ja')
            problem = scraping.get_problem()
            scraping.change_url(add_id)
            problem = scraping.get_problem()
            scraping.change_difficulty()
            scraping.write_problem(problem)
            scraping = Scraping(url, number_of_problem, difficulty, 'en')
            problem = scraping.get_problem()
            scraping.change_url(add_id)
            problem = scraping.get_problem()
            scraping.change_difficulty()
            scraping.write_problem(problem)
        print(number_of_problem)
    
    for number_of_problem in range(64, 65):
        for difficulty in ['a', 'b', 'c', 'd']:
            scraping = Scraping(url, number_of_problem, difficulty, 'ja')
            problem = scraping.get_problem()
            scraping.write_problem(problem)
            scraping = Scraping(url, number_of_problem, difficulty, 'en')
            problem = scraping.get_problem()
            scraping.write_problem(problem)
        print(number_of_problem)

    # 12 -> 11
    add_id = change_add(add_id, 1)
    for number_of_problem in range(65, 70):
        for difficulty in ['a', 'b']:
            scraping = Scraping(url, number_of_problem, difficulty, 'ja')
            problem = scraping.get_problem()
            scraping.write_problem(problem)
            scraping = Scraping(url, number_of_problem, difficulty, 'en')
            problem = scraping.get_problem()
            scraping.write_problem(problem)

        # 実際はc,d
        for difficulty in ['a', 'b']:
            scraping = Scraping(url, number_of_problem, difficulty, 'ja')
            problem = scraping.get_problem()
            scraping.change_url(add_id)
            problem = scraping.get_problem()
            scraping.change_difficulty()
            scraping.write_problem(problem)
            scraping = Scraping(url, number_of_problem, difficulty, 'en')
            problem = scraping.get_problem()
            scraping.change_url(add_id)
            problem = scraping.get_problem()
            scraping.change_difficulty()
            scraping.write_problem(problem)
        print(number_of_problem)
    
    for number_of_problem in range(70, 71):
        for difficulty in ['a', 'b', 'c', 'd']:
            scraping = Scraping(url, number_of_problem, difficulty, 'ja')
            problem = scraping.get_problem()
            scraping.write_problem(problem)
            scraping = Scraping(url, number_of_problem, difficulty, 'en')
            problem = scraping.get_problem()
            scraping.write_problem(problem)
        print(number_of_problem)

    # 11 -> 10
    add_id = change_add(add_id, 1)
    for number_of_problem in range(71, 73):
        for difficulty in ['a', 'b']:
            scraping = Scraping(url, number_of_problem, difficulty, 'ja')
            problem = scraping.get_problem()
            scraping.write_problem(problem)
            scraping = Scraping(url, number_of_problem, difficulty, 'en')
            problem = scraping.get_problem()
            scraping.write_problem(problem)

        # 実際はc,d
        for difficulty in ['a', 'b']:
            scraping = Scraping(url, number_of_problem, difficulty, 'ja')
            problem = scraping.get_problem()
            scraping.change_url(add_id)
            problem = scraping.get_problem()
            scraping.change_difficulty()
            scraping.write_problem(problem)
            scraping = Scraping(url, number_of_problem, difficulty, 'en')
            problem = scraping.get_problem()
            scraping.change_url(add_id)
            problem = scraping.get_problem()
            scraping.change_difficulty()
            scraping.write_problem(problem)
        print(number_of_problem)
    
    for number_of_problem in range(73, 74):
        for difficulty in ['a', 'b', 'c', 'd']:
            scraping = Scraping(url, number_of_problem, difficulty, 'ja')
            problem = scraping.get_problem()
            scraping.write_problem(problem)
            scraping = Scraping(url, number_of_problem, difficulty, 'en')
            problem = scraping.get_problem()
            scraping.write_problem(problem)
        print(number_of_problem)

    # 10 -> 9
    add_id = change_add(add_id, 1)
    for number_of_problem in range(74, 75):
        for difficulty in ['a', 'b']:
            scraping = Scraping(url, number_of_problem, difficulty, 'ja')
            problem = scraping.get_problem()
            scraping.write_problem(problem)
            scraping = Scraping(url, number_of_problem, difficulty, 'en')
            problem = scraping.get_problem()
            scraping.write_problem(problem)

        # 実際はc,d
        for difficulty in ['a', 'b']:
            scraping = Scraping(url, number_of_problem, difficulty, 'ja')
            problem = scraping.get_problem()
            scraping.change_url(add_id)
            problem = scraping.get_problem()
            scraping.change_difficulty()
            scraping.write_problem(problem)
            scraping = Scraping(url, number_of_problem, difficulty, 'en')
            problem = scraping.get_problem()
            scraping.change_url(add_id)
            problem = scraping.get_problem()
            scraping.change_difficulty()
            scraping.write_problem(problem)
        print(number_of_problem)
    
    for number_of_problem in range(75, 77):
        for difficulty in ['a', 'b', 'c', 'd']:
            scraping = Scraping(url, number_of_problem, difficulty, 'ja')
            problem = scraping.get_problem()
            scraping.write_problem(problem)
            scraping = Scraping(url, number_of_problem, difficulty, 'en')
            problem = scraping.get_problem()
            scraping.write_problem(problem)
        print(number_of_problem)

    # 9 -> 7
    add_id = change_add(add_id, 2)
    for number_of_problem in range(77, 79):
        for difficulty in ['a', 'b']:
            scraping = Scraping(url, number_of_problem, difficulty, 'ja')
            problem = scraping.get_problem()
            scraping.write_problem(problem)
            scraping = Scraping(url, number_of_problem, difficulty, 'en')
            problem = scraping.get_problem()
            scraping.write_problem(problem)

        # 実際はc,d
        for difficulty in ['a', 'b']:
            scraping = Scraping(url, number_of_problem, difficulty, 'ja')
            problem = scraping.get_problem()
            scraping.change_url(add_id)
            problem = scraping.get_problem()
            scraping.change_difficulty()
            scraping.write_problem(problem)
            scraping = Scraping(url, number_of_problem, difficulty, 'en')
            problem = scraping.get_problem()
            scraping.change_url(add_id)
            problem = scraping.get_problem()
            scraping.change_difficulty()
            scraping.write_problem(problem)
        print(number_of_problem)
    
    for number_of_problem in range(79, 81):
        for difficulty in ['a', 'b', 'c', 'd']:
            scraping = Scraping(url, number_of_problem, difficulty, 'ja')
            problem = scraping.get_problem()
            scraping.write_problem(problem)
            scraping = Scraping(url, number_of_problem, difficulty, 'en')
            problem = scraping.get_problem()
            scraping.write_problem(problem)
        print(number_of_problem)

    # 7 -> 5
    add_id = change_add(add_id, 2)
    for number_of_problem in range(81, 84):
        for difficulty in ['a', 'b']:
            scraping = Scraping(url, number_of_problem, difficulty, 'ja')
            problem = scraping.get_problem()
            scraping.write_problem(problem)
            scraping = Scraping(url, number_of_problem, difficulty, 'en')
            problem = scraping.get_problem()
            scraping.write_problem(problem)

        # 実際はc,d
        for difficulty in ['a', 'b']:
            scraping = Scraping(url, number_of_problem, difficulty, 'ja')
            problem = scraping.get_problem()
            scraping.change_url(add_id)
            problem = scraping.get_problem()
            scraping.change_difficulty()
            scraping.write_problem(problem)
            scraping = Scraping(url, number_of_problem, difficulty, 'en')
            problem = scraping.get_problem()
            scraping.change_url(add_id)
            problem = scraping.get_problem()
            scraping.change_difficulty()
            scraping.write_problem(problem)
        print(number_of_problem)
    
    for number_of_problem in range(84, 86):
        for difficulty in ['a', 'b', 'c', 'd']:
            scraping = Scraping(url, number_of_problem, difficulty, 'ja')
            problem = scraping.get_problem()
            scraping.write_problem(problem)
            scraping = Scraping(url, number_of_problem, difficulty, 'en')
            problem = scraping.get_problem()
            scraping.write_problem(problem)
        print(number_of_problem)

    # 5 -> 3
    add_id = change_add(add_id, 2)
    for number_of_problem in range(86, 88):
        for difficulty in ['a', 'b']:
            scraping = Scraping(url, number_of_problem, difficulty, 'ja')
            problem = scraping.get_problem()
            scraping.write_problem(problem)
            scraping = Scraping(url, number_of_problem, difficulty, 'en')
            problem = scraping.get_problem()
            scraping.write_problem(problem)

        # 実際はc,d
        for difficulty in ['a', 'b']:
            scraping = Scraping(url, number_of_problem, difficulty, 'ja')
            problem = scraping.get_problem()
            scraping.change_url(add_id)
            problem = scraping.get_problem()
            scraping.change_difficulty()
            scraping.write_problem(problem)
            scraping = Scraping(url, number_of_problem, difficulty, 'en')
            problem = scraping.get_problem()
            scraping.change_url(add_id)
            problem = scraping.get_problem()
            scraping.change_difficulty()
            scraping.write_problem(problem)
        print(number_of_problem)
    
    for number_of_problem in range(88, 90):
        for difficulty in ['a', 'b', 'c', 'd']:
            scraping = Scraping(url, number_of_problem, difficulty, 'ja')
            problem = scraping.get_problem()
            scraping.write_problem(problem)
            scraping = Scraping(url, number_of_problem, difficulty, 'en')
            problem = scraping.get_problem()
            scraping.write_problem(problem)
        print(number_of_problem)

    # 3 -> 1
    add_id = change_add(add_id, 2)
    for number_of_problem in range(90, 96):
        for difficulty in ['a', 'b']:
            scraping = Scraping(url, number_of_problem, difficulty, 'ja')
            problem = scraping.get_problem()
            scraping.write_problem(problem)
            scraping = Scraping(url, number_of_problem, difficulty, 'en')
            problem = scraping.get_problem()
            scraping.write_problem(problem)

        # 実際はc,d
        for difficulty in ['a', 'b']:
            scraping = Scraping(url, number_of_problem, difficulty, 'ja')
            problem = scraping.get_problem()
            scraping.change_url(add_id)
            problem = scraping.get_problem()
            scraping.change_difficulty()
            scraping.write_problem(problem)
            scraping = Scraping(url, number_of_problem, difficulty, 'en')
            problem = scraping.get_problem()
            scraping.change_url(add_id)
            problem = scraping.get_problem()
            scraping.change_difficulty()
            scraping.write_problem(problem)
        print(number_of_problem)
    
    for number_of_problem in range(96, 97):
        for difficulty in ['a', 'b', 'c', 'd']:
            scraping = Scraping(url, number_of_problem, difficulty, 'ja')
            problem = scraping.get_problem()
            scraping.write_problem(problem)
            scraping = Scraping(url, number_of_problem, difficulty, 'en')
            problem = scraping.get_problem()
            scraping.write_problem(problem)
        print(number_of_problem)

    # 1 -> 0
    add_id = change_add(add_id, 1)
    for number_of_problem in range(97, 99):
        for difficulty in ['a', 'b']:
            scraping = Scraping(url, number_of_problem, difficulty, 'ja')
            problem = scraping.get_problem()
            scraping.write_problem(problem)
            scraping = Scraping(url, number_of_problem, difficulty, 'en')
            problem = scraping.get_problem()
            scraping.write_problem(problem)

        # 実際はc,d
        for difficulty in ['a', 'b']:
            scraping = Scraping(url, number_of_problem, difficulty, 'ja')
            problem = scraping.get_problem()
            scraping.change_url(add_id)
            problem = scraping.get_problem()
            scraping.change_difficulty()
            scraping.write_problem(problem)
            scraping = Scraping(url, number_of_problem, difficulty, 'en')
            problem = scraping.get_problem()
            scraping.change_url(add_id)
            problem = scraping.get_problem()
            scraping.change_difficulty()
            scraping.write_problem(problem)
        print(number_of_problem)
    
    for number_of_problem in range(99, 101):
        for difficulty in ['a', 'b', 'c', 'd']:
            scraping = Scraping(url, number_of_problem, difficulty, 'ja')
            problem = scraping.get_problem()
            scraping.write_problem(problem)
            scraping = Scraping(url, number_of_problem, difficulty, 'en')
            problem = scraping.get_problem()
            scraping.write_problem(problem)
        print(number_of_problem)
    
    # 0 -> -2
    add_id = change_add(add_id, 2)
    
    for number_of_problem in range(101, 103):
        for difficulty in ['a', 'b']:
            scraping = Scraping(url, number_of_problem, difficulty, 'ja')
            problem = scraping.get_problem()
            scraping.write_problem(problem)
            scraping = Scraping(url, number_of_problem, difficulty, 'en')
            problem = scraping.get_problem()
            scraping.write_problem(problem)

        # 実際はc,d
        for difficulty in ['a', 'b']:
            scraping = Scraping(url, number_of_problem, difficulty, 'ja')
            problem = scraping.get_problem()
            scraping.change_url(add_id)
            problem = scraping.get_problem()
            scraping.change_difficulty()
            scraping.write_problem(problem)
            scraping = Scraping(url, number_of_problem, difficulty, 'en')
            problem = scraping.get_problem()
            scraping.change_url(add_id)
            problem = scraping.get_problem()
            scraping.change_difficulty()
            scraping.write_problem(problem)
        print(number_of_problem)

    for number_of_problem in range(103, 107):
        for difficulty in ['a', 'b', 'c', 'd']:
            scraping = Scraping(url, number_of_problem, difficulty, 'ja')
            problem = scraping.get_problem()
            scraping.write_problem(problem)
            scraping = Scraping(url, number_of_problem, difficulty, 'en')
            problem = scraping.get_problem()
            scraping.write_problem(problem)
        print(number_of_problem)

    # -2 -> -6
    add_id = change_add(add_id, 4)
    for number_of_problem in range(107, 109):
        for difficulty in ['a', 'b']:
            scraping = Scraping(url, number_of_problem, difficulty, 'ja')
            problem = scraping.get_problem()
            scraping.write_problem(problem)
            scraping = Scraping(url, number_of_problem, difficulty, 'en')
            problem = scraping.get_problem()
            scraping.write_problem(problem)

        # 実際はc,d
        for difficulty in ['a', 'b']:
            scraping = Scraping(url, number_of_problem, difficulty, 'ja')
            problem = scraping.get_problem()
            scraping.change_url(add_id)
            problem = scraping.get_problem()
            scraping.change_difficulty()
            scraping.write_problem(problem)
            scraping = Scraping(url, number_of_problem, difficulty, 'en')
            problem = scraping.get_problem()
            scraping.change_url(add_id)
            problem = scraping.get_problem()
            scraping.change_difficulty()
            scraping.write_problem(problem)
        print(number_of_problem)

    for number_of_problem in range(109, 111):
        for difficulty in ['a', 'b', 'c', 'd']:
            scraping = Scraping(url, number_of_problem, difficulty, 'ja')
            problem = scraping.get_problem()
            scraping.write_problem(problem)
            scraping = Scraping(url, number_of_problem, difficulty, 'en')
            problem = scraping.get_problem()
            scraping.write_problem(problem)
        print(number_of_problem)
    
    # -6 -> -8
    add_id = change_add(add_id, 2)
    for number_of_problem in range(111, 112):
        for difficulty in ['a', 'b']:
            scraping = Scraping(url, number_of_problem, difficulty, 'ja')
            problem = scraping.get_problem()
            scraping.write_problem(problem)
            scraping = Scraping(url, number_of_problem, difficulty, 'en')
            problem = scraping.get_problem()
            scraping.write_problem(problem)

        # 実際はc,d
        for difficulty in ['a', 'b']:
            scraping = Scraping(url, number_of_problem, difficulty, 'ja')
            problem = scraping.get_problem()
            scraping.change_url(add_id)
            problem = scraping.get_problem()
            scraping.change_difficulty()
            scraping.write_problem(problem)
            scraping = Scraping(url, number_of_problem, difficulty, 'en')
            problem = scraping.get_problem()
            scraping.change_url(add_id)
            problem = scraping.get_problem()
            scraping.change_difficulty()
            scraping.write_problem(problem)
        print(number_of_problem)

    for number_of_problem in range(112, 290):
        for difficulty in ['a', 'b', 'c', 'd']:
            scraping = Scraping(url, number_of_problem, difficulty, 'ja')
            problem = scraping.get_problem()
            scraping.write_problem(problem)
            scraping = Scraping(url, number_of_problem, difficulty, 'en')
            problem = scraping.get_problem()
            scraping.write_problem(problem)
        print(number_of_problem)
    #'''