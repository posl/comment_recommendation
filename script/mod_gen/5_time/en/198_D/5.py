def get_number(s, d):
    ret = 0
    for c in s:
        ret = ret * 10 + d[c]
    return ret

if __name__ == '__main__':
    get_number()