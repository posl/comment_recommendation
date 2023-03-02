import Levenshtein
import sys
import os
import re
import itertools
import pandas as pd

class Cal_Similarity():
    def __init__(self, path):
        self.path = path

    def get_path(self):
        self.path_l = os.listdir(self.path)
        self.path_l = sorted(self.path_l)
        return self.path_l
        
    def get_text(self, path):
        with open(path, 'r') as f:
            raw_text = f.readlines()
            raw_text_l = [s for s in raw_text if not s.startswith('#')]
            raw_text_l = list(map(lambda x: re.split('\n|\s', x), raw_text_l))
            text_l = []
            for i in raw_text_l:
                i = list(filter(lambda x: x != '', i))
                text_l.extend(i)
            text = ''.join(text_l)
        return text

    def get_similarity(self, l):
        sim_l = []
        for each_program in itertools.combinations(l, 2):
            each_sim = Levenshtein.ratio(each_program[0], each_program[1])
            sim_l.append(each_sim)
        return sim_l


if __name__ == '__main__':
    problem_l = os.listdir('../pre_research/')
    problem_l = sorted(problem_l)
    base_l = [i for i in range(1, 11)]
    com_l = list(itertools.combinations(base_l, 2))
    main_df = pd.DataFrame(index=com_l)
    for difficulty in ['a', 'b', 'c', 'd']:
        for problem in problem_l:
            path = '../pre_research/' + problem + '/' + difficulty + '/'
            cal = Cal_Similarity(path)
            program_path_l = cal.get_path()
            text_l = []
            for program_path in program_path_l:
                program_path = path + program_path
                text = cal.get_text(program_path)
                text_l.append(text)
            sim = cal.get_similarity(text_l)
            each_df = pd.DataFrame(sim, columns=[problem + difficulty], index=com_l)
            main_df = pd.concat([main_df, each_df], axis=1)
    
    main_df.to_csv('../result/similarity.csv')
