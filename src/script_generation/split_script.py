import os
import shutil

def detect_sign(l):
    index_l = []
    for index, content in enumerate(l):
        if content == '=======\n':
            index_l.append(index)
    return index_l

def split_script(base_l, l):
    script_l = []
    begin = 0
    for end in l:
        script_l.append(base_l[begin:end])
        begin = end + 1
    script_l.append(base_l[begin:])
    return script_l

if __name__ == '__main__':
    #which_close = 'test_close_app'
    print('input times')
    time = input() + '_time'
    language_l = []
    while True:
        print('input language (en, ja, zh, or end)')
        language = input()
        if language == 'end':
            break
        language_l.append(language)

    base_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

    for language in language_l:
        
        script_path = '{0}/script/post_gen/{1}/{2}/'.format(base_path, time, language)
        result_path = '{0}/script/split_gen/{1}/{2}/'.format(base_path, time, language)

        files_l = os.listdir(script_path)
        files_l = sorted(files_l)

        if os.path.exists(result_path + language + '_errors.txt'):
            os.remove(result_path + language + '_errors.txt')

        if os.path.exists(result_path):
            shutil.rmtree(result_path)
        
        os.mkdir(result_path)
        for file in files_l:
            '''
            if os.path.exists(result_path + file.split('problems')[1].split('.py')[0] + '/'):
                shutil.rmtree(result_path + file.split('problems')[1].split('.py')[0] + '/')
            '''
            difficulty = (file.split('problems')[1].split('.py')[0]).upper()
            new_dir_path = result_path + difficulty + '/'
            os.mkdir(new_dir_path)
            with open(script_path + file, 'r') as f:
                try:
                    for i in range(4):
                        next(f)
                    source_file_l = f.readlines()
                    source_file_l = list(map(lambda x: x.lstrip('\n'), source_file_l))
                    source_file_l = [i for i in source_file_l if not 'Suggestion' in i]
                    source_file_l = list(filter(None, source_file_l))
                    detect_sign_index_l = detect_sign(source_file_l)

                    all_script_l = split_script(source_file_l, detect_sign_index_l)

                    for index, each_script_l in enumerate(all_script_l):
                        with open(new_dir_path + str(index) + '.py', 'w') as f:
                            for line in each_script_l:
                                f.write(line)
                    print(file)
                except:
                    index = 0
                    if os.path.exists(result_path + language + '_errors.txt'):
                        with open(result_path + language + '_errors.txt', 'w') as f:
                            f.write(file + '\n')
                        with open(new_dir_path + str(index) + '.py', 'w') as f:
                            f.write('#')
                    else:
                        with open(result_path + language + '_errors.txt', 'a') as f:
                            f.write(file + '\n')
                        with open(new_dir_path + str(index) + '.py', 'w') as f:
                            f.write('#')
            #break