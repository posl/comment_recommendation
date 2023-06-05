def solve(n, l):
    ans = 0
    for i in range(n):
        ans += l + i
    return ans - l
