import csv
import os
import pandas as pd

class Target_complexity:
    def __init__(self, base_path, times, language, minimum, maximum):
        self.base_path = base_path
        self.result_path = base_path + '/result/target_complexity/{0}_{1}/{2}/{3}'.format(str(minimum), str(maximum), times, language)
        self.times = times
        self.language = language
        self.minimum = minimum
        self.maximum = maximum
        self.each_result_l = sorted(os.listdir('{0}/result/accuracy/each/{1}/{2}/'.format(self.base_path, self.times, self.language)))

    def target_complexity(self):
        all_target_l = []
        for each_result in self.each_result_l:
            main_df = pd.read_csv('{0}/result/accuracy/each/{1}/{2}/{3}'.format(self.base_path, self.times, self.language, each_result))
            df = main_df[(main_df['accuracy'] >= self.minimum) & (main_df['accuracy'] <= self.maximum)]
            df = df.iloc[:, 1:4]
            each_target_l = df.values.tolist()
            all_target_l.append(each_target_l)
        return all_target_l
    
    def write(self, all_l):
        for each_l in all_l:
            problem_number = str(each_l[0][0])
            if problem_number == '99':
                problem_number = '099'
                for i in range(len(each_l)):
                    each_l[i][0] = problem_number
            with open('{0}/{1}.txt'.format(self.result_path, problem_number), 'w') as f:
                for each_l_l in each_l:
                    f.write('{0},{1},{2}\n'.format(each_l_l[0], each_l_l[1], each_l_l[2]))
            print(problem_number)


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
    #print('input minimum')
    #minimum = float(input())
    minimum = float(1)
    #print('input maximum')
    maximum = float(1)
    if not os.path.exists('{0}/result/target_complexity/{1}_{2}/'.format(base_path, str(minimum), str(maximum))):
        os.mkdir('{0}/result/target_complexity/{1}_{2}/'.format(base_path, str(minimum), str(maximum)))
    target_complexity = Target_complexity(base_path, times, language, minimum, maximum)
    all_target_l = target_complexity.target_complexity()
    target_complexity.write(all_target_l)