import lizard
import os
import csv

class cal_cyclomatic_v2:
    def __init__(self, script_dir_base_path, target_base_each_l, result_path):
        self.script_dir_path = script_dir_base_path
        self.target_base_each_l = target_base_each_l
        self.result_path = result_path
    
    def main(self):
        all_result = []
        try:
            problem_number = self.target_base_each_l[0].split(',')[0]
            for script in self.target_base_each_l:
                each_result = []
                code = lizard.analyze_file('{0}/{1}_{2}/{3}.py'.format(self.script_dir_path, script.split(',')[0], script.split(',')[1], script.split(',')[2]))
                each_result.append(code.function_list[0].__dict__['cyclomatic_complexity'])
                each_result.append(code.function_list[0].__dict__['nloc'])
                each_result.append(code.function_list[0].__dict__['token_count'])
                #each_result.append(code.function_list[0].__dict__['parameter_count'])
                each_result.append(code.function_list[0].__dict__['filename'].split('/')[-1])
                all_result.append(each_result)
            #print(all_result)
            with open('{0}/{1}.csv'.format(self.result_path, problem_number), 'w') as f:
                writer = csv.writer(f)
                #writer.writerow(['cyclomatic_complexity', 'nloc', 'token_count', 'parameter_count', 'filename'])
                writer.writerow(['cyclomatic_complexity', 'nloc', 'token_count', 'filename'])
                writer.writerows(all_result)
        except:
            print('error')


if __name__ == '__main__':
    print('input times')
    times = input() + '_time'
    minimum = float(1)
    maximum = float(1)
    language_l = ['en', 'ja']
    base_path = '/Users/keikoyanagi/Desktop/comment_recommendation'
    
    for language in language_l:    
        script_dir_base_path = '{0}/script/mod_gen/{1}/{2}'.format(base_path, times, language)
        result_path = '{0}/result/cyclomatic/each/{1}/{2}'.format(base_path, times, language)
        target_base_path = '{0}/result/target_complexity/{1}_{2}/{3}/{4}'.format(base_path, str(minimum), str(maximum), times, language)
        #[099.txt, ~, 287.txt]
        target_base_l = sorted(os.listdir(target_base_path))
        for each_txt in target_base_l:
            with open('{0}/{1}'.format(target_base_path, each_txt), 'r') as f:
                #[[099,A,0], [099,A,1], ...]
                target_base_each_l = f.readlines()
                target_base_each_l = [each_txt.rstrip('\n') for each_txt in target_base_each_l]
            #print(target_base_each_l)
            a = cal_cyclomatic_v2(script_dir_base_path, target_base_each_l, result_path)
            a.main()
            print(each_txt.split('.')[0], language)
            break