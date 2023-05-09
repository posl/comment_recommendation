def solve(n, s):
    a = [0] * n
    for i in range(n - 1):
        a[i] = s[i] + a[i - 1]
    a[n - 1] = s[n - 1] + a[n - 2]
    return a
n = int(input())
s = list(map(int, input().split()))
print(*solve(n, s))

if __name__ == '__main__':
    solve()