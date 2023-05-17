import lizard
import os
import csv

class cal_cyclomatic_v2:
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
                code = lizard.analyze_file(self.base_path + self.script_dir_path + '/' + script)
                each_result.append(code.function_list[0].__dict__['cyclomatic_complexity'])
                each_result.append(code.function_list[0].__dict__['nloc'])
                each_result.append(code.function_list[0].__dict__['token_count'])
                #each_result.append(code.function_list[0].__dict__['parameter_count'])
                each_result.append(code.function_list[0].__dict__['filename'].split('/')[-1])
                all_result.append(each_result)
            #print(all_result)
            with open('{0}/{1}.csv'.format(self.result_path, self.script_dir_path.split('/')[-1]), 'w') as f:
                writer = csv.writer(f)
                #writer.writerow(['cyclomatic_complexity', 'nloc', 'token_count', 'parameter_count', 'filename'])
                writer.writerow(['cyclomatic_complexity', 'nloc', 'token_count', 'filename'])
                writer.writerows(all_result)
        except:
            print('error')


if __name__ == '__main__':
    print('input times')
    times = input() + '_time'
    language_l = ['en', 'ja']

    for language in language_l:
        base_path = '/Users/keikoyanagi/Desktop/comment_recommendation/script/mod_gen/{0}/{1}'.format(times, language)
        result_path = '/Users/keikoyanagi/Desktop/comment_recommendation/result/cyclomatic/each/{0}/{1}'.format(times, language)
        problem_l = sorted(os.listdir(base_path))
        for problem in problem_l:
            script_dir_path = '/{0}'.format(problem)
            a = cal_cyclomatic_v2(base_path, script_dir_path, result_path)
            a.main()
            print(problem, language)
            break