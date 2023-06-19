def find_index(s):
    def find_index(s, i):
        if len(s) == 1:
            return ord(s) - 64
        else:
            return 26 ** (len(s) - 1) * (ord(s[0]) - 64) + find_index(s[1:], i + 1)
    return find_index(s, 1)

if __name__ == '__main__':
    find_index()