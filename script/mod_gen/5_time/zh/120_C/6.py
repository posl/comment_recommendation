def solve():
    s = input()
    n = len(s)
    ans = 0
    for i in range(n):
        if s[i] == '1':
            ans += 1
    ans = min(ans, n-ans)
    print(ans)
solve()
