def solve():
    n,k = map(int, input().split())
    a = []
    for i in range(n):
        a.append(list(map(int, input().split())))
    a.sort()
    a = list(map(list, zip(*a)))
    a.sort()
    a = list(map(list, zip(*a)))
    ans = 10**9
    for i in range(n-k+1):
        for j in range(n-k+1):
            b = []
            for l in range(k):
                for m in range(k):
                    b.append(a[i+l][j+m])
            b.sort()
            ans = min(ans, b[(k*k)//2])
    print(ans)
