def do():
    n = int(input())
    s = []
    t = []
    for i in range(n):
        s.append(input())
    for i in range(n):
        t.append(input())
    for i in range(n):
        for j in range(n):
            if s[i][j] == '#':
                s[i] = s[i][j:] + s[i][:j]
                break
    for i in range(n):
        for j in range(n):
            if t[i][j] == '#':
                t[i] = t[i][j:] + t[i][:j]
                break
    for i in range(n):
        if s[i] != t[i]:
            print('No')
            return
    print('Yes')
