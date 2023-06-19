def get_same_num(a_list, b_list):
    same_num = 0
    for i in range(len(a_list)):
        if a_list[i] in b_list and a_list[i] == b_list[i]:
            same_num += 1
    return same_num

if __name__ == '__main__':
    get_same_num()