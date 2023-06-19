def get_index(s):
    length = len(s)
    if length == 1:
        return ord(s) - 64
    else:
        index = 0
        for i in range(length):
            index += (ord(s[i]) - 64) * (26 ** (length - i - 1))
        return index
