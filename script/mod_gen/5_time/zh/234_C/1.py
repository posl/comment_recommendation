def get_num(k):
    if k == 1:
        return 2
    else:
        return 10 * get_num(k-1) + 2

if __name__ == '__main__':
    get_num()