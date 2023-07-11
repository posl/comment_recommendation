import os
import re
import shutil

if __name__ == '__main__':
    base_path = '/Users/keikoyanagi/Desktop/comment_recommendation'
    path = '/script/pre_gen/zh'
    result_path = '/script/pre_gen/zh_mod'
    files_l = ['112_a', '115_a', '117_b', '119_a', '123_a', '141_a', '147_a', '150_a', '154_a', '154_c',  
               '155_a', '155_c', '159_b', '161_b', '162_a', '162_d', '164_a', '164_b', '164_c', '179_a', 
               '181_a', '181_d', '187_c', '190_a', '200_d', '201_d', '210_b', '212_a', '215_a', '218_a', 
               '219_a', '237_a', '238_a', '239_c', '239_d', '245_a', '249_a', '253_a', '261_b', '264_b', 
               '267_a', '283_d', '284_b', '284_d', '286_b']

    for file in files_l:
        shutil.copyfile('{0}/problems{1}.py'.format(base_path + path, file), '{0}/problems{1}.py'.format(base_path + result_path, file))
        print(file)