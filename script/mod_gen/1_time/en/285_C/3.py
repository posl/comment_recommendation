def get_index(s):
    if len(s) == 1:
        return ord(s) - ord('A') + 1
    else:
        return 26 + get_index(s[1:]) + 26 ** (len(s) - 1) * (ord(s[0]) - ord('A'))

if __name__ == '__main__':
    get_index()