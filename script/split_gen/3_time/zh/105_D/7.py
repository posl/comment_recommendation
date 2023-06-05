def problem105_d():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    s = [0]
    for i in range(n):
        s.append(s[i] + a[i])
    s = [x % m for x in s]
    s.sort()
    ans = 0
    prev = 0
    cnt = 0
    for x in s:
        if x == prev:
            cnt += 1
        else:
            ans += cnt * (cnt - 1) // 2
            prev = x
            cnt = 1
    ans += cnt * (cnt - 1) // 2
    print(ans)
