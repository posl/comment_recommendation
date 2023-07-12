import csv
import os
import pandas as pd

class Sum_each_accuracy:
    def __init__(self, base_path, times, language):
        self.base_path = base_path
        self.result_path = base_path + '/result/accuracy/all/{0}/{1}/'.format(times, language)
        self.times = times
        self.language = language
        self.each_result_l = sorted(os.listdir('{0}/result/accuracy/each/{1}/{2}/'.format(self.base_path, self.times, self.language)))
        

    def sum_accuracy(self):
        all_result_l = [[], [], [], []]
        for each_result in self.each_result_l:
            main_df = pd.read_csv('{0}/result/accuracy/each/{1}/{2}/{3}'.format(self.base_path, self.times, self.language, each_result))
            problem_number = each_result.split('_')[0]
            for i, difficulty in enumerate(['A', 'B', 'C', 'D']):
                df = main_df[main_df['difficulty'] == difficulty]
                pass_num = len(df[df['accuracy'] == 1])
                total_num = len(df)
                if (pass_num == total_num) and (pass_num != 0):
                    each_result_l = [problem_number, pass_num, total_num, 1]
                elif pass_num == 0:
                    each_result_l = [problem_number, pass_num, total_num, 0]
                else:
                    each_result_l = [problem_number, pass_num, total_num]
                all_result_l[i].append(each_result_l)
            print(each_result) 
        return all_result_l
    
    def write(self, all_result_l):
        os.makedirs(self.result_path, exist_ok=True)
        for i, difficulty in enumerate(['A', 'B', 'C', 'D']):
            with open('{0}/{1}_sum_accuracy.csv'.format(self.result_path, difficulty), 'w') as f:
                writer = csv.writer(f)
                writer.writerow(['problem_number', 'pass_num', 'total_num', 'accuracy'])
                for each_result_l in all_result_l[i]:
                    writer.writerow(each_result_l)

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
        sum_accuracy = Sum_each_accuracy(base_path, times, language)
        sum_accuracy_l = sum_accuracy.sum_accuracy()
        sum_accuracy.write(sum_accuracy_l)
    
