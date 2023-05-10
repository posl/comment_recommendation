def solve():
    n, k = map(int, input().split())
    s = input()
    s = list(s)
    s = list(map(int, s))
    cnt = 0
    for i in range(n-1):
        if s[i] == s[i+1]:
            cnt += 1
    ans = min(cnt + 2 * k, n - 1)
    print(ans)
