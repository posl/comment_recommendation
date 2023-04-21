import subprocess
import os
import openpyxl
import glob

class test_script:
    def __init__(self, script_path, input_path, output_path):
        self.script_path = script_path
        self.input_path = input_path
        self.output_path = output_path

    def pyexe(self):
        cmd = f'exec python {self.script_path} < {self.input_path}'
        try:
            p = subprocess.run(cmd, shell = True, capture_output = True, timeout = 30, text = True)
            output = p.stdout
            output.encode('utf-8')
            message = p.stderr
        
        except subprocess.TimeoutExpired as e:
            output = 'Timeout'
            message = 'TimeoutExpired'

        with open(self.output_path, encoding = 'utf-8') as f:
            test_case_text = f.read()
        
        if output == test_case_text:
            test = True
        else:
            test = False
        test_result = [test, output, test_case_text, message]

        return test_result
    
if __name__ == '__main__':
    a = test_script('/Users/keikoyanagi/Desktop/comment_recommendation/test_close_app/script/mod_gen/en/problems101_a_1.py', '/Users/keikoyanagi/Desktop/comment_recommendation/test_case/ABC101/A/in/1.txt', '/Users/keikoyanagi/Desktop/comment_recommendation/test_case/ABC101/A/out/1.txt')
    print(a.pyexe())