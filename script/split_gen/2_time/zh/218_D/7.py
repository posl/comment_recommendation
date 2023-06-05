def problem218_c():
    n = int(input())
    s = []
    t = []
    for i in range(n):
        s.append(input())
    for i in range(n):
        t.append(input())
    def rotate(x):
        return list(zip(*x[::-1]))
    def check():
        for i in range(n):
            for j in range(n):
                if s[i][j] != t[i][j]:
                    return False
        return True
    for i in range(4):
        if check():
            print('Yes')
            return
        t = rotate(t)
    print('No')
