def solve():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()
    b.sort()
    i = 0
    j = 0
    min_diff = 2 * 10 ** 9
    while i < n and j < m:
        min_diff = min(min_diff, abs(a[i] - b[j]))
        if a[i] < b[j]:
            i += 1
        else:
            j += 1
    print(min_diff)
solve()
