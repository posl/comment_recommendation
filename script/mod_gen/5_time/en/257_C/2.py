def solve():
    n = int(input())
    s = input()
    w = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        if s[i] == '1':
            ans += w[i]
    ans2 = ans
    for i in range(n):
        if s[i] == '1':
            ans2 -= w[i]
            ans = max(ans, ans2)
        else:
            ans2 += w[i]
            ans = max(ans, ans2)
    print(ans)
solve()
