import csv
import os
import pandas as pd

class Div_accuracy:
    def __init__(self, base_path, times, language):
        self.base_path = base_path
        self.result_path = base_path + '/result/accuracy/all/{0}/{1}/'.format(times, language)
        self.times = times
        self.language = language
        self.each_result_l = sorted(os.listdir('{0}/result/accuracy/each/{1}/{2}/'.format(self.base_path, self.times, self.language)))
        

    def div_accuracy(self):
        div_accuracy_l = [[0 for i in range(11)], [0 for i in range(11)], [0 for i in range(11)], [0 for i in range(11)]]
        for each_result in self.each_result_l:
            main_df = pd.read_csv('{0}/result/accuracy/each/{1}/{2}/{3}'.format(self.base_path, self.times, self.language, each_result))

            for i, difficulty in enumerate(['A', 'B', 'C', 'D']):
                df = main_df[main_df['difficulty'] == difficulty]
                df = df['accuracy']
                div = pd.cut(df,  bins=[0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6,0.7, 0.8, 0.9, 1.0, 1.1], right=False)
                div = div.value_counts(sort=False).tolist()
                for j in range(len(div)):
                    div_accuracy_l[i][j] += div[j]
        return div_accuracy_l
        
    
    def write(self, div_accuracy_l):
        with open('{0}/div_ratio_accuracy.csv'.format(self.result_path), 'w') as f:
            writer = csv.writer(f)
            percentage_l = []
            for percentage in range(0, 110, 10):
                percentage_l.append(str(percentage) + '%')
            writer.writerow(['difficulty'] + percentage_l)
            for i, difficulty in enumerate(['A', 'B', 'C', 'D']):
                writer.writerow([difficulty] + div_accuracy_l[i])

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
        div_accuracy = Div_accuracy(base_path, times, language)
        div_accuracy_l = div_accuracy.div_accuracy()
        div_accuracy.write(div_accuracy_l)