def get_max_num(a, b, c, d):
    max_num = a
    if b > max_num:
        max_num = b
    if c > max_num:
        max_num = c
    if d > max_num:
        max_num = d
    return max_num

if __name__ == '__main__':
    get_max_num()