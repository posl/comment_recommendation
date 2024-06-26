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

class specific_test_script:
    def __init__(self, script_path, input_path, output_path, all_result_path, accu_result_path):
        self.script_path = script_path
        self.input_path = input_path
        self.input_path_l = sorted(os.listdir(input_path))
        self.input_path_l = sorted(self.input_path_l, key = len)
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
        seg_test_case_l = []

        if flag == 'check':
            print(self.input_path_l)
            print('input fault number')
            fault_number = int(input())
            self.input_path_l = self.input_path_l[fault_number:]
            print(self.input_path_l)
        else:
            if times == '2_time':
                seg_test_case_l = ['3.txt', '7.txt', '8.txt', '11.txt', '12.txt', '14.txt', '16.txt', '17.txt', '19.txt', '20.txt', '21.txt', '23.txt', '27.txt', '29.txt', '33.txt']
            elif times == '5_time':
                seg_test_case_l = ['006.txt']
            if not len(seg_test_case_l) == 0:
                for delete_number in seg_test_case_l:
                    self.input_path_l.remove(delete_number)
        self.input_path_l = sorted(self.input_path_l)
        self.input_path_l = sorted(self.input_path_l, key = len)
        for i, each_test_case in enumerate(self.input_path_l):
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
                per_accuracy = accuracy / (len(self.input_path_l) + len(seg_test_case_l))
                each_test_result = [self.language, self.problem_number, self.difficulty, self.suggestion, self.input_path_l[i].split('.')[0], result, output, expected_output, message, per_accuracy]
                accuracy_l.append(accuracy)
                accuracy_l.append(len(self.input_path_l) + len(seg_test_case_l))
                accuracy_l.append(per_accuracy)
            else:
                each_test_result = [self.language, self.problem_number, self.difficulty, self.suggestion, self.input_path_l[i].split('.')[0], result, output, expected_output, message]

            with open('{0}/{1}_{2}_{3}_{4}.csv'.format(self.all_result_path, self.problem_number, self.difficulty, self.suggestion, each_test_case.split('.')[0]), 'w') as f:
                writer = csv.writer(f)
                writer.writerow(each_test_result)
            
            print(each_test_case)

        with open('{0}/{1}_seg_accuracy.csv'.format(self.accu_result_path, self.problem_number), 'a') as f:
            writer = csv.writer(f)
            writer.writerow(accuracy_l)

        
        with open('{0}/{1}_{2}_others.csv'.format(self.all_result_path, self.problem_number, self.difficulty), 'a') as f:
                writer = csv.writer(f)
                for each_test_case in seg_test_case_l:
                    each_test_result = [self.language, self.problem_number, self.difficulty, self.suggestion, each_test_case.split('.')[0], 0, '', '', 'segmentation fault']
                    writer.writerow(each_test_result)
          

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
    
    base_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

    if not os.path.exists('{0}/result/accuracy/each/{1}/{2}'.format(base_path, times, language)):
        os.makedirs('{0}/result/accuracy/each/{1}/{2}'.format(base_path, times, language))
    if not os.path.exists('{0}/result/ALL/{1}/{2}'.format(base_path, times, language)):
        os.makedirs('{0}/result/ALL/{1}/{2}'.format(base_path, times, language))
    # 2_time 111_D
    # seg_test_case_num = 3, 7, 8, 11, 12, 14, 16, 17, 19, 20, 21, 23, 27, 29, 33, 
    # 5_time 234_D
    # seg_test_case_num = 006, 

    if times == '2_time':
        problem_l = ['111_D']
    elif times == '5_time':
        problem_l = ['234_D']

    if flag == 'check':
        print('find suggestion or test?')
        flag2 = input()
        if flag2 == 'suggestion':
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
        
        elif flag2 == 'test':
            if times == '2_time':
                suggestion_number = 5
            elif times == '5_time':
                suggestion_number = 5
            else:
                print('input suggestion number')
                suggestion_number = int(input())
            for each_problem in problem_l:
                input_path = '{0}/test_case/ABC{1}/{2}/in/'.format(base_path, each_problem.split('_')[0], each_problem.split('_')[1])
                output_path = '{0}/test_case/ABC{1}/{2}/out/'.format(base_path, each_problem.split('_')[0], each_problem.split('_')[1])
                all_result_path = '{0}/result/ALL/{1}/{2}/'.format(base_path, times, language)
                accu_result_path = '{0}/result/accuracy/each/{1}/{2}/'.format(base_path, times, language)
                each_suggestion_l = sorted(os.listdir('{0}/script/mod_gen/{1}/{2}/{3}'.format(base_path, times, language, each_problem)))
                script_path = '{0}/script/mod_gen/{1}/{2}/{3}/{4}'.format(base_path, times, language, each_problem, each_suggestion_l[suggestion_number])
                a = specific_test_script(script_path, input_path, output_path, all_result_path, accu_result_path)
                a.pyexe()
                print(each_suggestion_l[suggestion_number], language)
    
    else:
        for each_problem in problem_l:
            # modify list in this loop in order to exclude segmentation fault
            each_suggestion_l = sorted(os.listdir('{0}/script/mod_gen/{1}/{2}/{3}'.format(base_path, times, language, each_problem)))
            before_l = each_suggestion_l[:fault_number]
            after_l = each_suggestion_l[fault_number + 1:]
            input_path = '{0}/test_case/ABC{1}/{2}/in/'.format(base_path, each_problem.split('_')[0], each_problem.split('_')[1])
            test_case_num = len(os.listdir(input_path))
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

            script_path = '{0}/script/mod_gen/{1}/{2}/{3}/{4}'.format(base_path, times, language, each_problem, each_suggestion_l[fault_number])
            a = specific_test_script(script_path, input_path, output_path, all_result_path, accu_result_path)
            a.pyexe()
            print(each_suggestion_l[fault_number], language)
            for each_suggestion in after_l:
                script_path = '{0}/script/mod_gen/{1}/{2}/{3}/{4}'.format(base_path, times, language, each_problem, each_suggestion)
                a = test_script(script_path, input_path, output_path, all_result_path, accu_result_path)
                a.pyexe()
                print(each_suggestion, language)
            print(each_problem, language)