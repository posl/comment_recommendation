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
    which_close = 'test_close_app'
    base_path = '../../' + which_close + '/script/post_gen/en/'
    files_l = os.listdir(base_path)
    files_l = sorted(files_l)

    for language in ['en', 'ja']:
        if os.path.exists('../../' + which_close + '/script/split_gen/' + language + '_errors.txt'):
            os.remove('../../' + which_close + '/script/split_gen/' + language + '_errors.txt')
        shutil.rmtree('../../' + which_close + '/script/split_gen/' + language)
        
        os.mkdir('../../' + which_close + '/script/split_gen/' + language)
        base_path = '../../' + which_close + '/script/post_gen/{}/'.format(language)
        result_path = '../../' + which_close + '/script/split_gen/{}/'.format(language)
        for file in files_l:
            with open(base_path + file, 'r') as f:
                try:
                    for i in range(4):
                        next(f)
                    source_file_l = f.readlines()
                    source_file_l = list(map(lambda x: x.lstrip('\n'), source_file_l))
                    source_file_l = list(filter(None, source_file_l))
                    detect_sign_index_l = detect_sign(source_file_l)

                    all_script_l = split_script(source_file_l, detect_sign_index_l)

                    for index, each_script_l in enumerate(all_script_l):
                        with open(result_path + file.replace('.py', '_' + str(index + 1) + '.py'), 'w') as f:
                            for line in each_script_l:
                                f.write(line)
                    print(file)
                except:
                    if os.path.exists('../../' + which_close + '/script/split_gen/' + language + '_errors.txt'):
                        with open('../../' + which_close + '/script/split_gen/' + language + '_errors.txt', 'w') as f:
                            f.write(file + '\n')
                        with open(result_path + file, 'w') as f:
                            f.write('#')
                    else:
                        with open('../../' + which_close + '/script/split_gen/' + language + '_errors.txt', 'a') as f:
                            f.write(file + '\n')
                        with open(result_path + file, 'w') as f:
                            f.write('#')
                            