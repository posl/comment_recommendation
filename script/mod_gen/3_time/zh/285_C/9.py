def get_index(s):
    if len(s) == 1:
        return ord(s) - ord('A') + 1
    else:
        if len(s) == 2:
            return 26 + get_index(s[1])
        else:
            return 26 + 26 + get_index(s[2:])

if __name__ == '__main__':
    get_index()