def solve():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    s.sort()
    ans = 0
    cnt = 0
    for i in range(n):
        if i > 0 and s[i] == s[i-1]:
            cnt += 1
        else:
            ans += cnt * (cnt + 1) // 2
            cnt = 0
    ans += cnt * (cnt + 1) // 2
    print(ans)
