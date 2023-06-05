def get_next_num(num):
    if num == 0:
        return 1
    elif num == 1:
        return 2
    elif num == 2:
        return 4
    else:
        return num*2

if __name__ == '__main__':
    get_next_num()