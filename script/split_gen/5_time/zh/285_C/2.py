def get_index(s):
    l = len(s)
    if l == 1:
        return ord(s) - ord('A') + 1
    else:
        index = 0
        for i in range(l-1):
            index += 26 ** (i+1)
        return index + get_index(s[1:]) + 1
