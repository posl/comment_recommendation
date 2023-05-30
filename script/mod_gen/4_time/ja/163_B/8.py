def solve():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    s = sum(a)
    if s < n:
        return -1
    for i in range(m):
        if a[i] < n:
            return i + 1
    return m
print(solve())
