def main():
    n, m = map(int, input().split())
    B = [list(map(int, input().split())) for _ in range(n)]
    for i in range(n):
        for j in range(m):
            B[i][j] -= i * 7
    for i in range(n):
        for j in range(m):
            if B[i][j] < 1 or B[i][j] > 7:
                print('No')
                return
    print('Yes')
