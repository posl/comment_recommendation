def solve():
    n, m, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    for i in range(n - 1):
        a[i + 1] += a[i]
    for i in range(m - 1):
        b[i + 1] += b[i]
    ans = 0
    j = m
    for i in range(n + 1):
        if a[i] > k:
            break
        while j > 0 and a[i] + b[j - 1] > k:
            j -= 1
        ans = max(ans, i + j)
    print(ans)

if __name__ == '__main__':
    solve()