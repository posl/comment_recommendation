def solve():
    s = input()
    t = input()
    n = len(s)
    ans = n
    for i in range(n):
        for j in range(n):
            if i + j >= n:
                break
            if s[i + j] != t[j]:
                break
            if i + j == n - 1:
                ans = min(ans, i)
    print(ans)
solve()
