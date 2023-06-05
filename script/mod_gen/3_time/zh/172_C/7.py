def solve():
    n, m, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    # 累计和
    for i in range(1, n):
        a[i] += a[i - 1]
    for i in range(1, m):
        b[i] += b[i - 1]
    ans = 0
    j = m - 1
    for i in range(n):
        if a[i] > k:
            break
        while j >= 0 and a[i] + b[j] > k:
            j -= 1
        ans = max(ans, i + j + 2)
    print(ans)

if __name__ == '__main__':
    solve()