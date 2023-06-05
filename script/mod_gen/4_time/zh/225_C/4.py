def solve():
    n, m = map(int, input().split())
    b = [list(map(int, input().split())) for _ in range(n)]
    for i in range(n):
        for j in range(m):
            b[i][j] -= i * 7 + j + 1
    b.sort()
    for i in range(n - 1):
        for j in range(m):
            if b[i][j] == b[i + 1][j]:
                return "No"
    return "Yes"
print(solve())
