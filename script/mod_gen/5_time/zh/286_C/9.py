def solve():
    n, a, b = map(int, input().split())
    s = input()
    s = list(s)
    ans = 0
    for i in range(n // 2):
        if s[i] == s[n - 1 - i]:
            continue
        elif s[i] == 'a':
            s[n - 1 - i] = 'a'
            ans += a
        elif s[n - 1 - i] == 'a':
            s[i] = 'a'
            ans += a
        else:
            print(-1)
            return
    if n % 2 == 1 and s[n // 2] != 'a':
        s[n // 2] = 'a'
        ans += a
    for i in range(n):
        if s[i] != 'a':
            ans += b
    print(ans)
solve()
