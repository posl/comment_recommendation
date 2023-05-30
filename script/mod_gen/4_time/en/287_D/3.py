def solve():
    s = input()
    t = input()
    n = len(s)
    m = len(t)
    for i in range(n-m+1):
        for j in range(m):
            if s[i+j] != '?' and s[i+j] != t[j]:
                break
        else:
            print('Yes')
            return
    print('No')
solve()
