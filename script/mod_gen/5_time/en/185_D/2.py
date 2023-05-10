def solve():
    n, m = map(int, input().split())
    if m == 0:
        return 1
    a = list(map(int, input().split()))
    a.sort()
    if a[0] != 1:
        a.insert(0, 0)
    if a[-1] != n:
        a.append(n+1)
    k = n
    for i in range(m+1):
        k = min(k, a[i+1] - a[i] - 1)
    ans = 0
    for i in range(m+1):
        ans += (a[i+1] - a[i] - 1) // k
        if (a[i+1] - a[i] - 1) % k:
            ans += 1
    return ans
print(solve())

if __name__ == '__main__':
    solve()