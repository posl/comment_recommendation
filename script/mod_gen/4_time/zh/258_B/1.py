def get_max_num(list):
    max_num = 0
    for i in range(len(list)):
        max_num += list[i] * (10 ** (len(list) - i - 1))
    return max_num

if __name__ == '__main__':
    get_max_num()