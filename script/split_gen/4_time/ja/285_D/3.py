def solve():
    n = int(input())
    s = []
    t = []
    for i in range(n):
        s_i, t_i = input().split()
        s.append(s_i)
        t.append(t_i)
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if s[i] == t[j]:
                print('No')
                return
    print('Yes')
    return
