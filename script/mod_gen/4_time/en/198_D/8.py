def get_int(s, d):
    num = 0
    for c in s:
        num = num * 10 + d[c]
    return num

if __name__ == '__main__':
    get_int()