def get_num(s):
    num = 0
    for i in s:
        num = num * 10 + ord(i) - ord('a')
    return num

if __name__ == '__main__':
    get_num()