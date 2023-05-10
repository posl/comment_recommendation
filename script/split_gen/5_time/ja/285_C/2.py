def get_num(s):
    if len(s) == 1:
        return ord(s) - ord('A') + 1
    elif len(s) == 2:
        return (ord(s[0]) - ord('A') + 1)*26 + ord(s[1]) - ord('A') + 1
    elif len(s) == 3:
        return (ord(s[0]) - ord('A') + 1)*26*26 + (ord(s[1]) - ord('A') + 1)*26 + ord(s[2]) - ord('A') + 1
    else:
        return 10000000000000000
