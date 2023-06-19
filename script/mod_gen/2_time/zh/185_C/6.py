def get_num(l):
    if l == 12:
        return 1
    elif l == 13:
        return 12
    else:
        return get_num(l-1) + get_num(l-2) + get_num(l-3) + get_num(l-4)

if __name__ == '__main__':
    get_num()