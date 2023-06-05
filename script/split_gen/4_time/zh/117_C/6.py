def solve():
    n, m = map(int, input().split())
    x = list(map(int, input().split()))
    x.sort()
    if n >= m:
        return 0
    d = []
    for i in range(m - 1):
        d.append(x[i + 1] - x[i])
    d.sort()
    return sum(d[:m - n])
print(solve())
