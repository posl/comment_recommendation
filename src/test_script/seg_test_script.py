import subprocess
import os
import openpyxl
import glob
import csv
import shutil

class test_script:
    def __init__(self, script_path, input_path, output_path, result_path):
        self.script_path = script_path
        self.input_path = input_path
        self.input_path_l = sorted(os.listdir(input_path))
        self.output_path = output_path
        self.output_path_l = sorted(os.listdir(output_path))
        self.result_path = result_path
        self.problem_number = script_path.split('/')[-2].split('_')[0]
        self.difficulty = script_path.split('/')[-2].split('_')[1]
        self.suggestion = script_path.split('/')[-1].split('.')[0]
        self.language = script_path.split('/')[-3]

    def pyexe(self):
        #all_test_result = []
        accuracy = 0
        for i in range(len(self.input_path_l)):
            each_input_path = self.input_path + self.input_path_l[i]
            #print(each_input_path)
            each_output_path = self.output_path + self.output_path_l[i]

            cmd = f'exec python {self.script_path} < {each_input_path}'
            try:
                p = subprocess.run(cmd, shell = True, capture_output = True, timeout = 30, text = True)
                output = p.stdout
                output.encode('utf-8')
                message = p.stderr
            
            except subprocess.TimeoutExpired as e:
                output = ''
                message = 'TimeoutExpired'

            with open(each_output_path, encoding = 'utf-8') as f:
                expected_output = f.read()
            
            if output == expected_output:
                result = 1
            else:
                result = 0
            accuracy += result

            if i == len(self.input_path_l) - 1:
                accuracy = accuracy / len(self.input_path_l)
                each_test_result = [self.language, self.problem_number, self.difficulty, self.suggestion, self.input_path_l[i].split('.')[0], result, output, expected_output, message, accuracy]
            else:
                each_test_result = [self.language, self.problem_number, self.difficulty, self.suggestion, self.input_path_l[i].split('.')[0], result, output, expected_output, message]

            with open('{0}/{1}.csv'.format(self.result_path, self.problem_number), 'a') as f:
                writer = csv.writer(f)
                writer.writerow(each_test_result)
    
    def write(self):
        with open('{0}/{1}.csv'.format(self.result_path, self.problem_number), 'w') as f:
            writer = csv.writer(f)
            writer.writerow(['language', 'problem_number', 'difficulty', 'suggestion', 'test_case', 'result', 'output', 'expected_output', 'message', 'accuracy'])
            #writer.writerows(l)

if __name__ == '__main__':
    # delete csv file and make new one with header
    print('input times')
    times = input() + '_time'
    print('choose language (en, ja, or zh)')
    language = input()

    if not os.path.exists('/Users/keikoyanagi/Desktop/comment_recommendation/result/accuracy/each/{0}/{1}'.format(times, language)):
        os.makedirs('/Users/keikoyanagi/Desktop/comment_recommendation/result/accuracy/each/{0}/{1}'.format(times, language))
    # 2_time 111_D
    problem_l = []

    for each_problem in problem_l:
        # modify list in this loop in order to exclude segmentation fault
        each_suggestion_l = sorted(os.listdir('/Users/keikoyanagi/Desktop/comment_recommendation/script/mod_gen/{0}/{1}/{2}'.format(times, language, each_problem)))
        #each_suggestion_l.remove('seg_test.py')
        for each_suggestion in each_suggestion_l:
            script_path = '/Users/keikoyanagi/Desktop/comment_recommendation/script/mod_gen/{0}/{1}/{2}/{3}'.format(times, language, each_problem, each_suggestion)
            input_path = '/Users/keikoyanagi/Desktop/comment_recommendation/test_case/ABC{0}/{1}/in/'.format(each_problem.split('_')[0], each_problem.split('_')[1])
            output_path = '/Users/keikoyanagi/Desktop/comment_recommendation/test_case/ABC{0}/{1}/out/'.format(each_problem.split('_')[0], each_problem.split('_')[1])
            result_path = '/Users/keikoyanagi/Desktop/comment_recommendation/result/accuracy/each/{0}/{1}/'.format(times, language)
            a = test_script(script_path, input_path, output_path, result_path)
            a.write()
            a.pyexe()
            print(each_suggestion, language)
        print(each_problem, language)
        #break
    