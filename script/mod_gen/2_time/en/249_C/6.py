def solve(n, k, s):
    ans = 0
    for i in range(2 ** n):
        t = []
        for j in range(n):
            if ((i >> j) & 1):
                t.append(s[j])
        t = ''.join(t)
        if len(set(t)) == k:
            ans = max(ans, len(t))
    return ans
n, k = map(int, input().split())
s = [input() for _ in range(n)]
print(solve(n, k, s))

if __name__ == '__main__':
    solve()