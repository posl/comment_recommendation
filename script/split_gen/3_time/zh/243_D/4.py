def get_index(n, x, s):
    index = x
    for i in range(n):
        if s[i] == 'U':
            index = index // 2
        elif s[i] == 'L':
            index = index * 2
        else:
            index = index * 2 + 1
    return index
