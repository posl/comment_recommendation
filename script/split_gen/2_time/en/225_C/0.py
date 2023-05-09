def main():
    n, m = map(int, input().split())
    b = [list(map(int, input().split())) for _ in range(n)]
    for i in range(n):
        for j in range(m):
            b[i][j] -= i * 7
    for i in range(1, n):
        if b[i][0] != b[i - 1][0] + 7:
            print('No')
            return
    for j in range(1, m):
        if b[0][j] != b[0][j - 1] + 1:
            print('No')
            return
    print('Yes')
