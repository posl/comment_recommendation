def get_max(a_list):
    max_num = 0
    for i in range(1, max(a_list)+1):
        tmp = 0
        for j in a_list:
            tmp += i % j
        if tmp > max_num:
            max_num = tmp
    return max_num

if __name__ == '__main__':
    get_max()