def test():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    for i in range(n - 1):
        for j in range(n - 1):
            if s[i][j] == '#' and s[i][j + 1] == '#' and s[i + 1][j] == '#' and s[i + 1][j + 1] == '#':
                s[i] = s[i][:j] + '1' + s[i][j + 1:]
                s[i] = s[i][:j + 1] + '1' + s[i][j + 2:]
                s[i + 1] = s[i + 1][:j] + '1' + s[i + 1][j + 1:]
                s[i + 1] = s[i + 1][:j + 1] + '1' + s[i + 1][j + 2:]
    for i in range(n):
        for j in range(n):
            if s[i][j] == '#':
                print('No')
                return
    print('Yes')
    return
test()
