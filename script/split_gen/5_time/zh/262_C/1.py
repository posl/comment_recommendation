def problems262_c():
    n = int(input())
    a = list(map(int, input().split()))
    l = [0]*(n+1)
    r = [0]*(n+1)
    for i in range(n):
        l[max(a[i], i+1)] += 1
        r[min(a[i], i+1)] += 1
    ans = 0
    for i in range(1, n+1):
        ans += l[i]*r[i]
    print(ans)
