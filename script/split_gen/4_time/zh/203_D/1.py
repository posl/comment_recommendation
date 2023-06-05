def solution():
    n, k = map(int, input().split())
    a = []
    for i in range(n):
        a.append(list(map(int, input().split())))
    m = k*k//2+1
    ans = 10**9
    for i in range(n-k+1):
        for j in range(n-k+1):
            b = []
            for p in range(k):
                for q in range(k):
                    b.append(a[i+p][j+q])
            b.sort()
            ans = min(ans, b[m-1])
    print(ans)
