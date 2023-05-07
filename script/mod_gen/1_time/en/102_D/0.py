def solve(n, a):
    s = [0] * (n + 1)
    for i in range(1, n + 1):
        s[i] = s[i - 1] + a[i - 1]
    ans = float('inf')
    for i in range(1, n - 1):
        for j in range(i + 1, n):
            ans = min(ans, abs(s[i] - s[0] - (s[j] - s[i]) - (s[n] - s[j])))
    return ans
n = int(input())
a = list(map(int, input().split()))
print(solve(n, a))

if __name__ == '__main__':
    solve()