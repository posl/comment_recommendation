def solve():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        a1,b1 = map(int,input().split())
        a.append(a1)
        b.append(b1)
    res = 0
    for i in range(n-1,-1,-1):
        a[i] += res
        if a[i]%b[i] == 0:
            continue
        res += b[i] - a[i]%b[i]
    print(res)
solve()
