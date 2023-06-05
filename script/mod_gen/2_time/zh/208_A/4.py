def solve():
    n = int(input())
    s = []
    t = []
    for i in range(n):
        s.append(list(map(int, input().split())))
    for i in range(n):
        t.append(list(map(int, input().split())))
    s.sort()
    t.sort()
    for i in range(n):
        for j in range(n):
            if s[i][0] == t[j][0] and s[i][1] == t[j][1]:
                break
        else:
            print('No')
            return
    for i in range(n):
        s[i][0] -= t[0][0]
        s[i][1] -= t[0][1]
    for i in range(n):
        for j in range(n):
            if s[i][0] == t[j][0] and s[i][1] == t[j][1]:
                break
        else:
            print('No')
            return
    print('Yes')
solve()
