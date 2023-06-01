import csv
import os
import pandas as pd

class Div_qty:
    def __init__(self, base_path, times, language):
        self.base_path = base_path
        self.result_path = base_path + '/result/accuracy/all/{0}/{1}/'.format(times, language)
        self.times = times
        self.language = language
        self.each_result_l = sorted(os.listdir('{0}/result/accuracy/each/{1}/{2}/'.format(self.base_path, self.times, self.language)))

    def div_qty(self):
        div_qty_df = pd.DataFrame(index=[], columns=[])
        div_qty_A_df = pd.DataFrame(index=[], columns=[])
        div_qty_B_df = pd.DataFrame(index=[], columns=[])
        div_qty_C_df = pd.DataFrame(index=[], columns=[])
        div_qty_D_df = pd.DataFrame(index=[], columns=[])

        for each_result in self.each_result_l:
            main_df = pd.read_csv('{0}/result/accuracy/each/{1}/{2}/{3}'.format(self.base_path, self.times, self.language, each_result))

            for i, difficulty in enumerate(['A', 'B', 'C', 'D']):
                df = main_df[main_df['difficulty'] == difficulty]
                df = pd.DataFrame((df['all_test_case_number'] - df['test_case_number']).value_counts(sort=False)).T
                
                if difficulty == 'A':
                    div_qty_A_df = pd.concat([div_qty_A_df, df])
                    div_qty_A_df.fillna(0)
                    div_qty_A_df = pd.DataFrame(div_qty_A_df.sum(axis=0)).T
                    div_qty_A_df.index = [difficulty]
                elif difficulty == 'B':
                    div_qty_B_df = pd.concat([div_qty_B_df, df])
                    div_qty_B_df.fillna(0)
                    div_qty_B_df = pd.DataFrame(div_qty_B_df.sum(axis=0)).T
                    div_qty_B_df.index = [difficulty]
                elif difficulty == 'C':
                    div_qty_C_df = pd.concat([div_qty_C_df, df])
                    div_qty_C_df.fillna(0)
                    div_qty_C_df = pd.DataFrame(div_qty_C_df.sum(axis=0)).T
                    div_qty_C_df.index = [difficulty]
                elif difficulty == 'D':
                    div_qty_D_df = pd.concat([div_qty_D_df, df])
                    div_qty_D_df.fillna(0)
                    div_qty_D_df = pd.DataFrame(div_qty_D_df.sum(axis=0)).T
                    div_qty_D_df.index = [difficulty]

        div_qty_df = pd.concat([div_qty_A_df, div_qty_B_df, div_qty_C_df, div_qty_D_df])
        div_qty_df = div_qty_df.fillna(0)
        div_qty_df = div_qty_df.sort_index(axis=1, ascending=False)

        return div_qty_df
    
    def write(self, div_qty_df):
        div_qty_df.to_csv('{0}/div_qty_accuracy.csv'.format(self.result_path))
    
if __name__ == '__main__':
    base_path = '/Users/keikoyanagi/Desktop/comment_recommendation'
    print('input times')
    times = input() + '_time'
    print('input language')
    language = input()
    div_qty = Div_qty(base_path, times, language)
    div_qty_l = div_qty.div_qty()
    div_qty.write(div_qty_l)