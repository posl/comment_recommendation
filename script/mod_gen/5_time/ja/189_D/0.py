def solve(n, s):
    ans = 1
    for c in s:
        if c == 'OR':
            ans += pow(2, n)
        n -= 1
    return ans
n = int(input())
s = [input() for _ in range(n)]
print(solve(n, s))
