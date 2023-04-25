import os
import shutil

def main(read_path, write_path):
    with open(read_path, 'r') as f:
        script_l = f.readlines()
        #print(script_l[0])
        try:
            if script_l[0].split(' ')[0] == 'def':
                function_name = script_l[0].split(' ')[1].split('(')[0]
                script_l.append('\nif __name__ == \'__main__\':\n' + '    ' + function_name + '()')
            with open(write_path, 'w') as f:
                for line in script_l:
                    f.write(line)
        except:
            pass

if __name__ == '__main__':
    time = '1_time'
    del_dir_path = '/Users/keikoyanagi/Desktop/comment_recommendation/script/mod_gen/{0}/'.format(time)
    if os.path.exists(del_dir_path):
        shutil.rmtree(del_dir_path)
        os.mkdir(del_dir_path)

    for language in ['en', 'ja']:
    #for language in ['zh']:
        base_path = '/Users/keikoyanagi/Desktop/comment_recommendation/script/split_gen/{0}/{1}/'.format(time, language)
        result_path = '/Users/keikoyanagi/Desktop/comment_recommendation/script/mod_gen/{0}/{1}/'.format(time, language)
        
        os.mkdir(result_path)

        each_files_l = os.listdir(base_path)
        each_files_l = sorted(each_files_l)

        for file in each_files_l:
            main(base_path + file, result_path + file)
            print(file)
            break