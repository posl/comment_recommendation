def solve():
    n = int(input())
    a = list(map(int, input().split()))
    s = sum(a)
    a = [0] + a
    for i in range(1, n + 1):
        a[i] += a[i - 1]
    ans = 10 ** 18
    for i in range(1, n - 2):
        for j in range(i + 1, n - 1):
            x = a[i]
            y = a[j] - a[i]
            z = a[n] - a[j]
            ans = min(ans, max(x, y, z) - min(x, y, z))
    print(ans)

if __name__ == '__main__':
    solve()