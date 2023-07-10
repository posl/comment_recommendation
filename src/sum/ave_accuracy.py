import csv
import os
import pandas as pd

class Ave_accuracy:
    def __init__(self, base_path, language):
        self.base_path = base_path
        self.result_path = base_path + '/result/accuracy/all/average/{0}/'.format(language)
        self.language = language
        self.each_result = base_path + '/result/accuracy/all'
        

    def sum_accuracy(self):
        self.a_df = pd.DataFrame(columns=['difficulty', 'pass_num', 'total_num', 'accuracy'])
        self.b_df = pd.DataFrame(columns=['difficulty', 'pass_num', 'total_num', 'accuracy'])
        self.c_df = pd.DataFrame(columns=['difficulty', 'pass_num', 'total_num', 'accuracy'])
        self.d_df = pd.DataFrame(columns=['difficulty', 'pass_num', 'total_num', 'accuracy'])
        for each_result in range(1, 6):
            each_df = pd.read_csv('{0}/{1}_time/{2}/sum_accuracy.csv'.format(self.each_result, str(each_result), self.language))

            for i, difficulty in enumerate(['A', 'B', 'C', 'D']):
                df = each_df[each_df['difficulty'] == difficulty]
                if difficulty == 'A':
                    self.a_df = pd.concat([self.a_df, df])
                elif difficulty == 'B':
                    self.b_df = pd.concat([self.b_df, df])
                elif difficulty == 'C':
                    self.c_df = pd.concat([self.c_df, df])
                elif difficulty == 'D':
                    self.d_df = pd.concat([self.d_df, df])
                
        for i in [self.a_df, self.b_df, self.c_df, self.d_df]:
            j = i.astype({'pass_num': int, 'total_num': int})
            i.loc['average'] = j.sum(numeric_only=True)/5
        return 
    
    def write(self):
        os.makedirs(self.result_path, exist_ok=True)
        self.a_df.to_csv('{0}/A.csv'.format(self.result_path), index=False)
        self.b_df.to_csv('{0}/B.csv'.format(self.result_path), index=False)
        self.c_df.to_csv('{0}/C.csv'.format(self.result_path), index=False)
        self.d_df.to_csv('{0}/D.csv'.format(self.result_path), index=False)

    

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
        ave_accuracy = Ave_accuracy(base_path, language)
        ave_accuracy_l = ave_accuracy.sum_accuracy()
        ave_accuracy.write()
    
