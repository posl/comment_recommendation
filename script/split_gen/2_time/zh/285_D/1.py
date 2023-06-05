def get_index(s):
    n = len(s)
    if n == 1:
        return ord(s) - ord('A') + 1
    elif n == 2:
        return 26 + (ord(s[0]) - ord('A')) * 26 + (ord(s[1]) - ord('A')) + 1
    else:
        return 26 + 26 * 26 + (ord(s[0]) - ord('A')) * 26 * 26 + (ord(s[1]) - ord('A')) * 26 + (ord(s[2]) - ord('A')) + 1
