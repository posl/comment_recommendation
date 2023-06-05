def get_max_num(str):
    max_num = 0
    for s in str:
        if int(s) > max_num:
            max_num = int(s)
    return max_num

if __name__ == '__main__':
    get_max_num()