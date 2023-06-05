def get_num(s):
    if len(s) == 1:
        return ord(s) - ord('A') + 1
    else:
        return (ord(s[0]) - ord('A') + 1) * 26 ** (len(s) - 1) + get_num(s[1:])
