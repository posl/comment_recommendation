import csv
import os
import pandas as pd

class Sum_accuracy:
    def __init__(self, base_path, times, language):
        self.base_path = base_path
        self.result_path = base_path + '/result/accuracy/all/{0}/{1}/'.format(times, language)
        self.times = times
        self.language = language
        self.each_result_l = sorted(os.listdir('{0}/result/accuracy/each/{1}/{2}/'.format(self.base_path, self.times, self.language)))
        

    def sum_accuracy(self):
        sum_accuracy_l = [[0, 0], [0, 0], [0, 0], [0, 0]]
        for each_result in self.each_result_l:
            main_df = pd.read_csv('{0}/result/accuracy/each/{1}/{2}/{3}'.format(self.base_path, self.times, self.language, each_result))

            for i, difficulty in enumerate(['A', 'B', 'C', 'D']):
                df = main_df[main_df['difficulty'] == difficulty]
                pass_num = len(df[df['accuracy'] == 1])
                total_num = len(df)
                sum_accuracy_l[i][0] += pass_num
                sum_accuracy_l[i][1] += total_num
            print(each_result) 
        return sum_accuracy_l
    
    def write(self, sum_accuracy_l):
        with open('{0}/sum_accuracy.csv'.format(self.result_path), 'w') as f:
            writer = csv.writer(f)
            writer.writerow(['difficulty', 'pass_num', 'total_num', 'accuracy'])
            for i, difficulty in enumerate(['A', 'B', 'C', 'D']):
                writer.writerow([difficulty, sum_accuracy_l[i][0], sum_accuracy_l[i][1], sum_accuracy_l[i][0] / sum_accuracy_l[i][1]])

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
    for language in language_l:
        sum_accuracy = Sum_accuracy(base_path, times, language)
        sum_accuracy_l = sum_accuracy.sum_accuracy()
        sum_accuracy.write(sum_accuracy_l)
    
