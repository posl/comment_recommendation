def solve():
    n = int(input())
    s = []
    t = []
    for i in range(n):
        s.append(list(map(int, input().split())))
    for i in range(n):
        t.append(list(map(int, input().split())))
    if n == 1:
        print('Yes')
        return
    for i in range(1, n):
        s[i][0] -= s[0][0]
        s[i][1] -= s[0][1]
        t[i][0] -= t[0][0]
        t[i][1] -= t[0][1]
    for i in range(n):
        for j in range(n):
            if s[i][0] == t[j][0] and s[i][1] == t[j][1]:
                for k in range(n):
                    s[k][0] += s[i][0]
                    s[k][1] += s[i][1]
                for k in range(n):
                    if s[k][0] != t[k][0] or s[k][1] != t[k][1]:
                        print('No')
                        return
                print('Yes')
                return
    print('No')
