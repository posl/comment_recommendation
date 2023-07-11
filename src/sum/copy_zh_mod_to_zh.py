import shutil
import os

if __name__ == '__main__':
    times = input() + '_time'
    base_path = '/Users/keikoyanagi/Desktop/comment_recommendation'
    path = '/result/accuracy/each/{0}/zh_mod/'.format(times)
    result_path = '/result/accuracy/each/{0}/zh/'.format(times)
    files_l = os.listdir(base_path + path)

    for file in files_l:
        shutil.copyfile(base_path + path + file, base_path + result_path + file)
        print(file)