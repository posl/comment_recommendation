import subprocess
import os
import openpyxl
import glob
import csv
import shutil

class test_script:
    def __init__(self, script_path, input_path, output_path, all_result_path, accu_result_path):
        self.script_path = script_path
        self.input_path = input_path
        self.input_path_l = sorted(os.listdir(input_path))
        self.output_path = output_path
        self.output_path_l = sorted(os.listdir(output_path))
        self.all_result_path = all_result_path
        self.accu_result_path = accu_result_path
        self.problem_number = script_path.split('/')[-2].split('_')[0]
        self.difficulty = script_path.split('/')[-2].split('_')[1]
        self.suggestion = script_path.split('/')[-1].split('.')[0]
        self.language = script_path.split('/')[-3]

    def pyexe(self):
        all_test_result = []
        accuracy_l = [self.language, self.problem_number, self.difficulty, self.suggestion]
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
                per_accuracy = accuracy / len(self.input_path_l)
                each_test_result = [self.language, self.problem_number, self.difficulty, self.suggestion, self.input_path_l[i].split('.')[0], result, output, expected_output, message, per_accuracy]
                accuracy_l.append(accuracy)
                accuracy_l.append(len(self.input_path_l))
                accuracy_l.append(per_accuracy)
            else:
                each_test_result = [self.language, self.problem_number, self.difficulty, self.suggestion, self.input_path_l[i].split('.')[0], result, output, expected_output, message]
            all_test_result.append(each_test_result)

        return all_test_result, accuracy_l
    
    def write(self, all_result, accuracy_l):
        with open('{0}/{1}_{2}.csv'.format(self.all_result_path, self.problem_number, self.difficulty), 'a') as f:
            writer = csv.writer(f)
            if self.suggestion == '0':
                writer.writerow(['language', 'problem_number', 'difficulty', 'suggestion', 'test_case', 'result', 'output', 'expected_output', 'message', 'accuracy'])
            writer.writerows(all_result)
        
        with open('{0}/{1}_accuracy.csv'.format(self.accu_result_path, self.problem_number), 'a') as f:
            writer = csv.writer(f)
            if (self.suggestion == '0') and (self.difficulty == 'A'):
                writer.writerow(['language', 'problem_number', 'difficulty', 'suggestion_number' ,'test_case_number', 'all_test_case_number', 'accuracy'])
            writer.writerow(accuracy_l)

if __name__ == '__main__':
    # delete csv file and make new one with header
    print('input times')
    times = input() + '_time'
    language_l = []
    while True:
        print('input language (en, ja, zh, zh_mod, or end)')
        language = input()
        if language == 'end':
            break
        language_l.append(language)
    base_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) 
    
    for language in language_l:
        if os.path.exists('{0}/result/ALL/{1}/{2}/'.format(base_path, times, language)):
            shutil.rmtree('{0}/result/ALL/{1}/{2}/'.format(base_path, times, language))
        os.mkdir('{0}/result/ALL/{1}/{2}/'.format(base_path, times, language))
        
        del_dir_path = '{0}/result/accuracy/each/{1}/{2}/'.format(base_path, times, language)
        if os.path.exists(del_dir_path):
            shutil.rmtree(del_dir_path)
        os.mkdir(del_dir_path)

        base_problem_l = sorted(os.listdir('{0}/script/mod_gen/{1}/{2}'.format(base_path, times, language)))
        #print(base_problem_l)
        problem_l = []
        for problem in base_problem_l:
            if os.path.isdir('{0}/script/mod_gen/{1}/{2}/{3}'.format(base_path, times, language, problem)):
                problem_l.append(problem)

        problem_l = sorted(problem_l)
        if (times == '2_time') and (language == 'en'):
            problem_l.remove('111_D')
        
        if (times == '5_time') and (language == 'ja'):
            problem_l.remove('234_D')
            #543 = 234_D
            #problem_l = problem_l[544:]
        if language == 'zh_mod':
            problem_l = ['112_a', '115_a', '117_b', '119_a', '123_a', '141_a', '147_a', '150_a', '154_a', '154_c',  
                         '155_a', '155_c', '159_b', '161_b', '162_a', '162_d', '164_a', '164_b', '164_c', '179_a', 
                         '181_a', '181_d', '187_c', '190_a', '200_d', '201_d', '210_b', '212_a', '215_a', '218_a', 
                         '219_a', '237_a', '238_a', '239_c', '239_d', '245_a', '249_a', '253_a', '261_b', '264_b', 
                         '267_a', '283_d', '284_b', '284_d', '286_b']
            for i in range(len(problem_l)):
                problem_l[i] = problem_l[i].upper()
        
        for each_problem in problem_l:
            base_each_suggestion_l = sorted(os.listdir('{0}/script/mod_gen/{1}/{2}/{3}'.format(base_path, times, language, each_problem)))
         
            for each_suggestion in sorted(os.listdir('{0}/script/mod_gen/{1}/{2}/{3}'.format(base_path, times, language, each_problem))):
                script_path = '{0}/script/mod_gen/{1}/{2}/{3}/{4}'.format(base_path, times, language, each_problem, each_suggestion)
                input_path = '{0}/test_case/ABC{1}/{2}/in/'.format(base_path, each_problem.split('_')[0], each_problem.split('_')[1])
                output_path = '{0}/test_case/ABC{1}/{2}/out/'.format(base_path, each_problem.split('_')[0], each_problem.split('_')[1])
                all_result_path = '{0}/result/ALL/{1}/{2}/'.format(base_path, times, language)
                accu_result_path = '{0}/result/accuracy/each/{1}/{2}/'.format(base_path, times, language)
                a = test_script(script_path, input_path, output_path, all_result_path, accu_result_path)
                a.write(a.pyexe()[0], a.pyexe()[1])
            print(each_problem, language)
            #break
    
