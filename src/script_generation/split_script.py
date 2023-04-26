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
    time = '1_time'

    base_path = '/Users/keikoyanagi/Desktop/comment_recommendation/script/post_gen/{0}/'.format(time)
    files_l = os.listdir(base_path + 'en')
    files_l = sorted(files_l)

    for language in ['en', 'ja']:
        
        base_path = '/Users/keikoyanagi/Desktop/comment_recommendation/script/post_gen/{0}/{1}/'.format(time, language)
        result_path = '/Users/keikoyanagi/Desktop/comment_recommendation/script/split_gen/{0}/{1}/'.format(time, language)

        if os.path.exists(result_path + language + '_errors.txt'):
            os.remove(result_path + language + '_errors.txt')
        shutil.rmtree(result_path)
        
        os.mkdir(result_path)
        for file in files_l:
            '''
            if os.path.exists(result_path + file.split('problems')[1].split('.py')[0] + '/'):
                shutil.rmtree(result_path + file.split('problems')[1].split('.py')[0] + '/')
            '''
            os.mkdir(result_path + file.split('problems')[1].split('.py')[0] + '/')
            with open(base_path + file, 'r') as f:
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
                        with open(result_path + file.split('problems')[1].split('.py')[0] + '/' + str(index) + '.py', 'w') as f:
                            for line in each_script_l:
                                f.write(line)
                    print(file)
                except:
                    if os.path.exists(result_path + language + '_errors.txt'):
                        with open(result_path + language + '_errors.txt', 'w') as f:
                            f.write(file + '\n')
                        with open(result_path + file.split('problems')[1].split('.py')[0] + '/' + str(index) + '.py', 'w') as f:
                            f.write('#')
                    else:
                        with open(result_path + language + '_errors.txt', 'a') as f:
                            f.write(file + '\n')
                        with open(result_path + file.split('problems')[1].split('.py')[0] + '/' + str(index) + '.py', 'w') as f:
                            f.write('#')
            #break