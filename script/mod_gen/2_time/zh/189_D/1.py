def solve(n, s):
    if n == 0:
        return 1
    elif s[n - 1] == 'AND':
        return solve(n - 1, s)
    elif s[n - 1] == 'OR':
        return 2 ** (n + 1) + solve(n - 1, s)
n = int(input())
s = [input() for _ in range(n)]
print(solve(n, s))
