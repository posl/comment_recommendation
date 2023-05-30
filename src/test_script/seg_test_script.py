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
        #all_test_result = []
        accuracy = 0
        accuracy_l = [self.language, self.problem_number, self.difficulty, self.suggestion]
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

            with open('{0}/{1}_{2}.csv'.format(self.all_result_path, self.problem_number, self.difficulty), 'a') as f:
                writer = csv.writer(f)
                writer.writerow(each_test_result)

        with open('{0}/{1}_seg_accuracy.csv'.format(self.accu_result_path, self.problem_number), 'a') as f:
            writer = csv.writer(f)
            writer.writerow(accuracy_l)        
    
    def write(self):
        with open('{0}/{1}_{2}.csv'.format(self.all_result_path, self.problem_number, self.difficulty), 'w') as f:
            writer = csv.writer(f)
            writer.writerow(['language', 'problem_number', 'difficulty', 'suggestion', 'test_case', 'result', 'output', 'expected_output', 'message', 'accuracy'])
            #writer.writerows(l)
        
        with open('{0}/{1}_seg_accuracy.csv'.format(self.accu_result_path, self.problem_number), 'w') as f:
            writer = csv.writer(f)
            writer.writerow(['language', 'problem_number', 'difficulty', 'suggestion_number' ,'test_case_number', 'all_test_case_number', 'accuracy'])

if __name__ == '__main__':
    # delete csv file and make new one with header
    print('input times')
    times = input() + '_time'
    print('choose language (en, ja, or zh)')
    language = input()
    print('input check or exec')
    flag = input()
    if flag == 'check':
        pass
    else:
        print('input fault number')
        fault_number = int(input())
    
    base_path = '/Users/keikoyanagi/Desktop/comment_recommendation'

    if not os.path.exists('{0}/result/accuracy/each/{1}/{2}'.format(base_path, times, language)):
        os.makedirs('{0}/result/accuracy/each/{1}/{2}'.format(base_path, times, language))
    if not os.path.exists('{0}/result/ALL/{1}/{2}'.format(base_path, times, language)):
        os.makedirs('{0}/result/ALL/{1}/{2}'.format(base_path, times, language))
    # 2_time 111_D
    problem_l = ['111_D']

    if flag == 'check':
        for each_problem in problem_l:
            # modify list in this loop in order to exclude segmentation fault
            each_suggestion_l = sorted(os.listdir('{0}/script/mod_gen/{1}/{2}/{3}'.format(base_path, times, language, each_problem)))
            print(each_suggestion_l)
            #each_suggestion_l.remove('seg_test.py')
            for count ,each_suggestion in enumerate(each_suggestion_l):
                script_path = '{0}/script/mod_gen/{1}/{2}/{3}/{4}'.format(base_path, times, language, each_problem, each_suggestion)
                input_path = '{0}/test_case/ABC{1}/{2}/in/'.format(base_path, each_problem.split('_')[0], each_problem.split('_')[1])
                output_path = '{0}/test_case/ABC{1}/{2}/out/'.format(base_path, each_problem.split('_')[0], each_problem.split('_')[1])
                all_result_path = '{0}/result/ALL/{1}/{2}/'.format(base_path, times, language)
                accu_result_path = '{0}/result/accuracy/each/{1}/{2}/'.format(base_path, times, language)
                a = test_script(script_path, input_path, output_path, all_result_path, accu_result_path)
                if count == 0:
                    a.write()
                a.pyexe()
                print(each_suggestion, language)
            print(each_problem, language)
            #break
    
    else:
        for each_problem in problem_l:
            # modify list in this loop in order to exclude segmentation fault
            each_suggestion_l = sorted(os.listdir('{0}/script/mod_gen/{1}/{2}/{3}'.format(base_path, times, language, each_problem)))
            before_l = each_suggestion_l[:fault_number]
            after_l = each_suggestion_l[fault_number + 1:]
            input_path = '{0}/test_case/ABC{1}/{2}/in/'.format(base_path, each_problem.split('_')[0], each_problem.split('_')[1])
            output_path = '{0}/test_case/ABC{1}/{2}/out/'.format(base_path, each_problem.split('_')[0], each_problem.split('_')[1])
            all_result_path = '{0}/result/ALL/{1}/{2}/'.format(base_path, times, language)
            accu_result_path = '{0}/result/accuracy/each/{1}/{2}/'.format(base_path, times, language)
            for count, each_suggestion in enumerate(before_l):
                script_path = '{0}/script/mod_gen/{1}/{2}/{3}/{4}'.format(base_path, times, language, each_problem, each_suggestion)
                a = test_script(script_path, input_path, output_path, all_result_path, accu_result_path)
                if count == 0:
                    a.write()
                a.pyexe()
                print(each_suggestion, language)
            
            with open('{0}/result/ALL/{1}/{2}/{3}.csv'.format(base_path, times, language, each_problem), 'a') as f:
                writer = csv.writer(f)
                writer.writerow([language, each_problem.split('_')[0], each_problem.split('_')[1], fault_number, '', 0, '', '', 'segmentation fault', 0])
            
            with open('{0}/result/accuracy/each/{1}/{2}/{3}_seg_accuracy.csv'.format(base_path, times, language, each_problem.split('_')[0]), 'a') as f:
                writer = csv.writer(f)
                writer.writerow([language, each_problem.split('_')[0], each_problem.split('_')[1], fault_number, '', '', 0])
            
            for each_suggestion in after_l:
                script_path = '{0}/script/mod_gen/{1}/{2}/{3}/{4}'.format(base_path, times, language, each_problem, each_suggestion)
                a = test_script(script_path, input_path, output_path, all_result_path, accu_result_path)
                a.pyexe()
                print(each_suggestion, language)
            print(each_problem, language)