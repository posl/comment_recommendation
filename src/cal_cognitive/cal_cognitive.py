import ast
from cognitive_complexity.api import get_cognitive_complexity
import os
import csv
import shutil

class cal_cognitive:
    def __init__(self, base_path, script_dir_path, result_path):
        self.base_path = base_path
        self.script_dir_path = script_dir_path
        self.result_path = result_path

    def main(self):
        all_result = []
        try:
            script_l = sorted(os.listdir(self.base_path + self.script_dir_path))
            for script in script_l:
                each_result = []
                with open(self.base_path + self.script_dir_path + '/' + script, 'r') as f:
                    tree = ast.parse(f.read())
                    result = get_cognitive_complexity(tree.body[0])
                    each_result.append(result)
                    each_result.append(script)
                    all_result.append(each_result)
            with open('{0}/{1}.csv'.format(self.result_path, self.script_dir_path.split('/')[-1]), 'w') as f:
                writer = csv.writer(f)
                writer.writerow(['cognitive_complexity', 'filename'])
                writer.writerows(all_result)
        except:
            print('error')

if __name__ == '__main__':
    print('input times')
    times = input() + '_time'
    language_l = ['en', 'ja']

    for language in language_l:
        del_dir_path = '/Users/keikoyanagi/Desktop/comment_recommendation/result/cognitive/each/{0}/{1}/'.format(times, language)
        if os.path.exists(del_dir_path):
            shutil.rmtree(del_dir_path)
        os.mkdir(del_dir_path)
        base_path = '/Users/keikoyanagi/Desktop/comment_recommendation/script/split_gen/{0}/{1}'.format(times, language)
        result_path = '/Users/keikoyanagi/Desktop/comment_recommendation/result/cognitive/each/{0}/{1}'.format(times, language)
        problem_l = sorted(os.listdir(base_path))
        for problem in problem_l:
            script_dir_path = '/{0}'.format(problem)
            a = cal_cognitive(base_path, script_dir_path, result_path)
            a.main()
            print(problem, language)
            break