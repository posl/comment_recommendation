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
    if os.path.exists('../../test_close_app/script/mod_gen'):
        shutil.rmtree('../../test_close_app/script/mod_gen')
        os.mkdir('../../test_close_app/script/mod_gen')
        os.mkdir('../../test_close_app/script/mod_gen/en/')
        os.mkdir('../../test_close_app/script/mod_gen/ja/')
        #os.mkdir('../../test_close_app/script/mod_gen/zh/')
    
    which_path = 'test_close_app'
    base_path = '../../' + which_path + '/script/split_gen/'
    result_path = '../../' + which_path + '/script/mod_gen/'

    en_files_l = os.listdir(base_path + 'en/')
    ja_files_l = os.listdir(base_path + 'ja/')
    en_files_l = sorted(en_files_l)
    ja_files_l = sorted(ja_files_l)

    for file in en_files_l:
        main(base_path + 'en/' + file, result_path + 'en/' + file)
        print(file)

    for file in ja_files_l:
        main(base_path + 'ja/' + file, result_path + 'ja/' + file)
        print(file)