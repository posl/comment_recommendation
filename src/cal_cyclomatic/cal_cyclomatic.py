import subprocess
import os

class cal_cyclomatic:
    def __init__(self, base_path, script_dir_path, result_path):
        self.base_path = base_path
        self.script_dir_path = script_dir_path
        self.result_path = result_path

    def main(self):
        #cd_cmd = "cd {0}".format(self.base_path + self.script_dir_path)
        cmd = "exec lizard -l python --csv > {0}/{1}_cyclomatic.csv".format(self.result_path, self.script_dir_path.split('/')[-1])
        try:
            p = subprocess.run(cmd, shell = True, capture_output = True, timeout = 30, text = True, cwd = self.base_path + self.script_dir_path)
        
        except subprocess.TimeoutExpired as e:
            print('timeout')
        
        return p.stdout


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
            a = cal_cyclomatic(base_path, script_dir_path, result_path)
            a.main()
            print(problem, language)
            #break
