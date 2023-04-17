import os

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
    base_path = '../../test_close_window/script/post_gen/en/'
    files_l = os.listdir(base_path)
    files_l = sorted(files_l)

    
    with open(base_path, 'r') as f:
        for i in range(4):
            next(f)
        source_file_l = f.readlines()
    source_file_l = list(map(lambda x: x.lstrip('\n'), source_file_l))
    source_file_l = list(filter(None, source_file_l))
    detect_sign_index_l = detect_sign(source_file_l)

    all_script_l = split_script(source_file_l, detect_sign_index_l)

    for index, each_script_l in enumerate(all_script_l):
        with open(result_path.replace('.py', '_' + str(index + 1) + '.py'), 'w') as f:
            for line in each_script_l:
                f.write(line)
    