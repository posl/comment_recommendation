import shutil
import os
import pandas as pd

if __name__ == '__main__':
    print('input times')
    times = input() + '_time'
    base_path = '/Users/keikoyanagi/Desktop/comment_recommendation'
    path = '/result/accuracy/each/{0}/zh_mod/'.format(times)
    result_path = '/result/accuracy/each/{0}/zh/'.format(times)
    files_l = os.listdir(base_path + path)
    files_l = sorted(files_l)


    for file in files_l:
        mod_df = pd.read_csv(base_path + path + file)
        base_df = pd.read_csv(base_path + result_path + file)

        #print(base_df)
        #print(mod_df)
        
        difficulty_l = ['A', 'B', 'C', 'D']
        remove_difficulty_l = mod_df['difficulty'].value_counts().index.tolist()
        #print(remove_difficulty_l)

        for difficulty in remove_difficulty_l:
            difficulty_l.remove(difficulty)

        #print(difficulty_l)

        for difficulty in difficulty_l:
            df = base_df[base_df['difficulty'] == difficulty]
            mod_df = pd.concat([mod_df, df])

        mod_df = mod_df.sort_values(by='difficulty')

        #print(mod_df)
        with open(base_path + result_path + file, 'w') as f:
            mod_df.to_csv(f, index=False)
        print(file)

        #break