def solve():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    print(a)
    for i in range(n):
        if i == 0:
            ans = a[i]
        else:
            ans += (a[i] - a[i-1] - 1)
    print(ans)
