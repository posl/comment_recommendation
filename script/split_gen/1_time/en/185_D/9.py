def  main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    a.append(n+1)
    cnt = []
    prev = 0
    for i in range(m+1):
        if a[i] - prev - 1 > 0:
            cnt.append(a[i] - prev - 1)
        prev = a[i]
    if len(cnt) == 0:
        print(0)
        return
    k = min(cnt)
    ans = 0
    for i in range(len(cnt)):
        ans += (cnt[i] - 1) // k + 1
    print(ans)
