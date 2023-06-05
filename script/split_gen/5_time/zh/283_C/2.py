def solve():
    s = input()
    n = len(s)
    ans = n
    for i in range(n-1):
        if s[i] == '1':
            ans = min(ans, i+n-1-i)
    print(ans)
solve()
