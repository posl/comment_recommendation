import csv
import pandas as pd
import os

class Summarize_at_least:
    def __init__(self, base_path, language):
        self.base_path = base_path
        self.language = language
        self.each_result = base_path + '/result/accuracy/all/at_least'
    
    def permutate_at_least(self):
        df = pd.read_csv('{0}/{1}_at_least.csv'.format(self.each_result, self.language))
        df = df.sort_values(['difficulty', 'times'], ascending=True, ignore_index=True)
        df.to_csv('{0}/per_{1}_at_least.csv'.format(self.each_result, self.language), index=False)
    
    def get_median(self):
        df = pd.read_csv('{0}/per_{1}_at_least.csv'.format(self.each_result, self.language))
        df = df.sort_values(['difficulty', 'times'], ascending=True, ignore_index=True).drop(['times', 'pass_num','total_num'], axis=1)
        df = df.groupby(['difficulty']).median().T
        df = df.rename(index={'accuracy': self.language})
        return df
        #df.to_csv('{0}/{1}_at_least_median.csv'.format(self.each_result, self.language), index=False)
        
    def make_table(self):
        df = pd.read_csv('{0}/per_{1}_at_least.csv'.format(self.each_result, self.language))
        df = df.reindex(columns=['times', 'difficulty', 'accuracy', 'pass_num', 'total_num'])
        df.drop(['difficulty'], axis=1, inplace=True)
        for i in range(len(df)):
            df.iloc[i, 1] = df.iloc[i, 1].round(3)
        df['proportion'] = df['pass_num'].astype(str) + ' / ' + df['total_num'].astype(str)
        df.drop(['pass_num', 'total_num'], axis=1, inplace=True)
        for i in range(4):
            each_df = df.iloc[i*5:(i+1)*5, :]
            each_df = each_df.reset_index(drop=True)
            if i == 0:
                all_df = each_df
            else:
                all_df = pd.concat([all_df, each_df.drop(['times'], axis = 1)], axis=1)
        
        all_df.to_csv('{0}/table_{1}_at_least.csv'.format(self.each_result, self.language), index=False)

if __name__ == '__main__':
    base_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    language_l = []
    while True:
        print('input language (en, ja, zh, or end)')
        language = input()
        if language == 'end':
            break
        language_l.append(language)
    for language in language_l:
        summarize_at_least = Summarize_at_least(base_path, language)
        summarize_at_least.permutate_at_least()
        each_df = summarize_at_least.get_median()
        df = summarize_at_least.make_table()
        all_df = each_df if language == language_l[0] else pd.concat([all_df, each_df], axis=0)
    all_df.to_csv('{0}/result/accuracy/all/at_least/at_least_median.csv'.format(base_path), index=True)