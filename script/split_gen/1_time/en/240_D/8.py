def solve():
    n = int(input())
    a = [int(x) for x in input().split()]
    ans = [0]*n
    d = {}
    for i in range(n):
        if a[i] in d:
            ans[i] = ans[d[a[i]]] + 1
        d[a[i]] = i
    print(*ans, sep='\n')
