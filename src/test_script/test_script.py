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
        all_test_result = []
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
            all_test_result.append(each_test_result)
        return all_test_result
    
    def write(self, l):
        '''
        if int(self.problem_number) < 119:
            file_number = '99_118'
        elif int(self.problem_number) < 139:
            file_number = '119_138'
        elif int(self.problem_number) < 159:
            file_number = '139_158'
        elif int(self.problem_number) < 179:
            file_number = '159_178'
        elif int(self.problem_number) < 199:
            file_number = '179_198'
        elif int(self.problem_number) < 219:
            file_number = '199_218'
        elif int(self.problem_number) < 239:
            file_number = '219_238'
        elif int(self.problem_number) < 259:
            file_number = '239_258'
        elif int(self.problem_number) < 279:
            file_number = '259_278'
        else:
            file_number = '279_287'
        '''
        with open('{0}/{1}.csv'.format(self.result_path, self.problem_number), 'w') as f:
            writer = csv.writer(f)
            writer.writerow(['language', 'problem_number', 'difficulty', 'suggestion', 'test_case', 'result', 'output', 'expected_output', 'message', 'accuracy'])
            writer.writerows(l)

if __name__ == '__main__':
    # delete csv file and make new one with header
    print('input times')
    times = input() + '_time'
    language_l = ['en', 'ja']
    
    for language in language_l:
        del_dir_path = '/Users/keikoyanagi/Desktop/comment_recommendation/result/accuracy/each/{0}/{1}/'.format(times, language)
        if os.path.exists(del_dir_path):
            shutil.rmtree(del_dir_path)
        os.mkdir(del_dir_path)

        '''
        start = 99
        for i in range(10):
            if i == 9:
                end = 287
            else:
                end = start + 19

            with open('{0}/{1}_{2}.csv'.format(del_dir_path, str(start), str(end)), 'w') as f:
                writer = csv.writer(f)
                writer.writerow(['language', 'problem_number', 'difficulty', 'suggestion', 'test_case', 'result', 'output', 'expected_output', 'message', 'accuracy'])
            start = end + 1
        '''

        base_problem_l = sorted(os.listdir('/Users/keikoyanagi/Desktop/comment_recommendation/script/mod_gen/{0}/{1}'.format(times, language)))
        problem_l = []
        for problem in base_problem_l:
            if os.path.isdir('/Users/keikoyanagi/Desktop/comment_recommendation/script/mod_gen/{0}/{1}/{2}'.format(times, language, problem)):
                problem_l.append(problem)

        problem_l = sorted(problem_l)
        if times == '2_time':
            problem_l.remove('111_D')
        for each_problem in problem_l:
            base_each_suggestion_l = sorted(os.listdir('/Users/keikoyanagi/Desktop/comment_recommendation/script/mod_gen/{0}/{1}/{2}'.format(times, language, each_problem)))
            '''
            each_suggestion_l = []
            for each_suggestion in base_each_suggestion_l:
                if os.path.isfile('/Users/keikoyanagi/Desktop/comment_recommendation/script/mod_gen/{0}/{1}/{2}/{3}'.format(times, language, each_problem, each_suggestion)):
                    each_suggestion_l.append(each_suggestion)
            '''
            for each_suggestion in sorted(os.listdir('/Users/keikoyanagi/Desktop/comment_recommendation/script/mod_gen/{0}/{1}/{2}'.format(times, language, each_problem))):
                script_path = '/Users/keikoyanagi/Desktop/comment_recommendation/script/mod_gen/{0}/{1}/{2}/{3}'.format(times, language, each_problem, each_suggestion)
                input_path = '/Users/keikoyanagi/Desktop/comment_recommendation/test_case/ABC{0}/{1}/in/'.format(each_problem.split('_')[0], each_problem.split('_')[1])
                output_path = '/Users/keikoyanagi/Desktop/comment_recommendation/test_case/ABC{0}/{1}/out/'.format(each_problem.split('_')[0], each_problem.split('_')[1])
                result_path = '/Users/keikoyanagi/Desktop/comment_recommendation/result/accuracy/each/{0}/{1}/'.format(times, language)
                a = test_script(script_path, input_path, output_path, result_path)
                a.write(a.pyexe())
            print(each_problem, language)
            #break
    
    '''
    a = test_script('/Users/keikoyanagi/Desktop/comment_recommendation/test_close_app/script/mod_gen/en/problems101_a_1.py', '/Users/keikoyanagi/Desktop/comment_recommendation/test_case/ABC101/A/in/1.txt', '/Users/keikoyanagi/Desktop/comment_recommendation/test_case/ABC101/A/out/1.txt')
    print(a.pyexe())
    '''