def solve():
    n,k = map(int,input().split())
    ans = 0
    for i in range(1,n+1):
        if i >= k:
            ans += 1/n
        else:
            point = 1
            while i*point < k:
                point *= 2
            ans += (1/n) * (1/point)
    print(ans)
