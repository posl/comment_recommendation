def calc(n, k, a, b):
    if n == 0:
        return 1 if k == 0 else 0
    elif k < 0:
        return 0
    else:
        return sum([calc(n-1, k-a[i][j], a, b) for j in range(n)])
n, k = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
print(calc(n, k, a, 0))
