def solve():
    n,m = map(int, input().split())
    if n == 1:
        return 0
    if n == 2:
        return 1
    x = list(map(int, input().split()))
    x.sort()
    d = [0]*(m-1)
    for i in range(m-1):
        d[i] = x[i+1] - x[i]
    d.sort()
    return sum(d[:m-n])
print(solve())
