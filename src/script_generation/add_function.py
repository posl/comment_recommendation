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
    print('input times')
    time = input() + '_time'
    del_dir_path = '/Users/keikoyanagi/Desktop/comment_recommendation/script/mod_gen/{0}/'.format(time)
    if os.path.exists(del_dir_path):
        shutil.rmtree(del_dir_path)
    os.mkdir(del_dir_path)

    for language in ['en', 'ja']:
    #for language in ['zh']:
        base_path = '/Users/keikoyanagi/Desktop/comment_recommendation/script/split_gen/{0}/{1}/'.format(time, language)
        result_path = '/Users/keikoyanagi/Desktop/comment_recommendation/script/mod_gen/{0}/{1}/'.format(time, language)
        
        os.mkdir(result_path)

        base_each_dir_l = os.listdir(base_path)
        #each_dir_l = list(map(lambda x: x if os.path.isdir(base_path + x) else '', base_each_dir_l))
        each_dir_l = []
        for dir in base_each_dir_l:
            if os.path.isdir(base_path + dir):
                each_dir_l.append(dir)
        each_dir_l = sorted(each_dir_l)
                
        for dir in each_dir_l:
            os.mkdir(result_path + dir + '/')

            each_files_l = os.listdir(base_path + dir + '/')
            each_files_l = sorted(each_files_l)

            for file in each_files_l:
                main(base_path + dir + '/' + file, result_path +  dir + '/' + file)
                #print(file)
                #break
            print(dir)