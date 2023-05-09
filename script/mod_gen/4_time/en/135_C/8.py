def solve(n, a, b):
    ans = 0
    for i in range(n):
        ans += min(a[i], b[i])
        b[i] -= min(a[i], b[i])
        ans += min(a[i + 1], b[i])
        a[i + 1] -= min(a[i + 1], b[i])
    ans += min(a[n], b[n - 1])
    return ans
n = int(input())
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
print(solve(n, a, b))

if __name__ == '__main__':
    solve()