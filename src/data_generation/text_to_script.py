import os
import re

if __name__ == '__main__':
    base_path = '../../data/en/'
    result_path = '../../script/en/'
    files_l = os.listdir(base_path)
    files_l = sorted(files_l)

    for language in ['en', 'ja','zh']:
        base_path = '../../data/{}/'.format(language)
        result_path = '../../script/{}/'.format(language)
        for file in files_l:
            with open(base_path + file, 'r') as f:
                source_file_l = f.readlines()
                source_file_l = list(map(lambda x: '#' + x, source_file_l))
                source_file_l.append('\ndef ')
            
            with open(result_path + file.replace('.txt', '.py'), 'w') as f:
                for line in source_file_l:
                    f.write(line)
            print(file)