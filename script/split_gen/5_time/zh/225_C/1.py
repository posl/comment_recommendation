def solve():
    n, m = map(int, input().split())
    b = []
    for i in range(n):
        b.append(list(map(int, input().split())))
    for i in range(1, n):
        for j in range(m):
            b[i][j] -= b[0][j]
    for i in range(m):
        if b[0][i] % 7 != 0:
            return False
    for i in range(1, n):
        for j in range(m):
            if b[i][j] % 7 != 0:
                return False
    return True
