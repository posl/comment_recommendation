def get_num(s):
    if len(s) == 1:
        return ord(s) - 64
    else:
        num = 0
        for i in range(len(s)):
            num += (ord(s[i]) - 64) * 26 ** (len(s) - i - 1)
        return num
