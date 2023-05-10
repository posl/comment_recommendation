def solve(n, c):
    c.sort()
    ans = 1
    for i in range(n):
        ans *= max(c[i] - i, 0)
        ans %= 10**9 + 7
    return ans
n = int(input())
c = list(map(int, input().split()))
print(solve(n, c))
