def solve():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    if m == 0:
        return 1
    min_k = n
    for i in range(m - 1):
        min_k = min(min_k, a[i + 1] - a[i] - 1)
    min_k = min(min_k, n - a[m - 1])
    ans = 0
    for i in range(m):
        ans += (a[i] + min_k - 1) // min_k
    return ans
print(solve())

if __name__ == '__main__':
    solve()