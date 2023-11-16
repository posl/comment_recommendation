import os
import shutil

def main(read_path, write_path):
    with open(read_path, 'r') as f:
        script_l = f.readlines()
        try:
            if script_l[0].split(' ')[0] == 'def':
                function_name = script_l[0].split(' ')[1].split('(')[0]
                
                if (function_name in script_l[-1]) and not('return' in script_l[-1]) and not('append' in script_l[-1]): #and not('print' in script_l[-1])
                    pass
                else:
                    script_l.append('\nif __name__ == \'__main__\':\n' + '    ' + function_name + '()')
                
            with open(write_path, 'w') as f:
                for line in script_l:
                    f.write(line)
        except:
            pass

if __name__ == '__main__':
    print('input times')
    time = input() + '_time'
    language_l = []
    while True:
        print('input language (en, ja, zh, or end)')
        language = input()
        if language == 'end':
            break
        language_l.append(language)

    for language in language_l:
        path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        base_path = '{0}/script/split_gen/{1}/{2}/'.format(path, time, language)
        result_path = '{0}/script/mod_gen/{1}/{2}/'.format(path, time, language)

        if os.path.exists(result_path):
            shutil.rmtree(result_path)
        
        os.mkdir(result_path)

        base_each_dir_l = os.listdir(base_path)
        each_dir_l = []
        for each_dir in base_each_dir_l:
            if os.path.isdir(base_path + each_dir):
                each_dir_l.append(each_dir)
        each_dir_l = sorted(each_dir_l)
                
        for each_dir in each_dir_l:
            os.mkdir(result_path + each_dir + '/')

            each_files_l = os.listdir(base_path + each_dir + '/')
            each_files_l = sorted(each_files_l)

            for file in each_files_l:
                main(base_path + each_dir + '/' + file, result_path +  each_dir + '/' + file)
                #print(file)
                #break
            print(each_dir)