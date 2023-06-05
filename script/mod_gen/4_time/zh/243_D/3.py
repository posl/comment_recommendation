def find_index(n, x, s):
    index = x
    for i in range(n):
        if s[i] == 'U':
            index = index // 2
        elif s[i] == 'L':
            index = index * 2
        else:
            index = index * 2 + 1
    return index

if __name__ == '__main__':
    find_index()