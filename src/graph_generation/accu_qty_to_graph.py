import csv
import pandas as pd
import matplotlib.pyplot as plt
import os

class Accu_to_graph:
    def __init__(self, base_path, target, times, language):
        self.target = target
        self.target_path = '{0}/result/accuracy/all/{1}/{2}/div_{3}_accuracy.csv'.format(base_path, times, language, target)
        self.times = times
        self.language = language
        self.result_path = '{0}/result/accuracy/graph/{1}/{2}/'.format(base_path, times, language)
        self.target_df = pd.read_csv(self.target_path, index_col=0).T
        os.makedirs(self.result_path.split(language)[0], exist_ok=True)
        os.makedirs(self.result_path, exist_ok=True)
    
    def accu_to_graph(self):
        pd.options.plotting.backend = 'matplotlib'
        self.target_df.plot(kind='bar', logy=False, stacked=False, rot=0, figsize=(20, 5), xlabel='error_test_case')
        plt.savefig('{0}/accu_{1}_graph.png'.format(self.result_path, self.target))

if __name__ == '__main__':
    base_path = '/Users/keikoyanagi/Desktop/comment_recommendation'
    print('input times')
    times = input() + '_time'

    language_l = []
    while True:
        print('input language (en, ja, zh, or end)')
        language = input()
        if language == 'end':
            break
        language_l.append(language)

    target_l = []
    while True:
        print('input target (qty, ratio, or end)')
        target = input()
        if target == 'end':
            break
        target_l.append(target)

    for language in language_l:
        for target in target_l:
            qty = Accu_to_graph(base_path, target, times, language)
            qty.accu_to_graph()