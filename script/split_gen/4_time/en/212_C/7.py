def solve():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()
    b.sort()
    ans = 10**9
    i = 0
    for j in range(m):
        while i < n - 1 and a[i] < b[j]:
            i += 1
        ans = min(ans, abs(a[i] - b[j]))
    print(ans)
