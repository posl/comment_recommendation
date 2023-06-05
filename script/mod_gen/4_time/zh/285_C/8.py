def get_num(s):
    if len(s) == 1:
        return ord(s) - 64
    else:
        return (ord(s[0]) - 64) * 26 + get_num(s[1:])

if __name__ == '__main__':
    get_num()