import csv
import os
import pandas as pd

class At_least_accuracy:
    def __init__(self, base_path, language):
        self.base_path = base_path
        self.language = language
        self.each_result = base_path + '/result/accuracy/all'

    def sum_accuracy(self):
        all_df = pd.DataFrame(columns=['times', 'difficulty', 'pass_num', 'total_num', 'accuracy'])
        for time in range(1, 6):
            each_df = pd.DataFrame(columns=['times', 'difficulty', 'pass_num', 'total_num', 'accuracy'])
            result_path = '{0}/{1}_time/{2}'.format(self.each_result, str(time), self.language)
            for difficulty in ['A', 'B', 'C', 'D']:
                base_df = pd.read_csv('{0}/{1}_time/{2}/{3}_sum_accuracy.csv'.format(self.each_result, str(time), self.language, difficulty))
                length = len(base_df)
                at_least = length - (base_df['pass_num'] == 0).sum()
                each_l = [time, difficulty, at_least, length, at_least / length]
                each_df = pd.concat([each_df, pd.DataFrame([each_l], columns=['times', 'difficulty', 'pass_num', 'total_num', 'accuracy'])], ignore_index=True)
            each_df.to_csv('{0}/at_least_accuracy.csv'.format(result_path), index=False)
            all_df = pd.concat([all_df, each_df], ignore_index=True)
        result_path = '{0}/at_least'.format(self.each_result, self.language)
        os.makedirs(result_path, exist_ok=True)
        all_df.to_csv('{0}/{1}_at_least.csv'.format(result_path, self.language), index=False)
            #break
        

if __name__ == '__main__':
    base_path = '/Users/keikoyanagi/Desktop/comment_recommendation'
    language_l = []
    while True:
        print('input language (en, ja, zh, or end)')
        language = input()
        if language == 'end':
            break
        language_l.append(language)
    for language in language_l:
        at_least_accuracy = At_least_accuracy(base_path, language)
        at_least_accuracy.sum_accuracy()