def main():
    N = int(input())
    A = [int(input()) for _ in range(N)]
    X = [[0] * N for _ in range(N)]
    Y = [[0] * N for _ in range(N)]
    for i in range(N):
        for _ in range(A[i]):
            x, y = map(int, input().split())
            X[i][x - 1] = y
            Y[i][x - 1] = y
    ans = 0
    for bit in range(1 << N):
        for i in range(N):
            for j in range(N):
                if i == j:
                    continue
                if (bit >> j) & 1 and X[i][j] == 0:
                    X[i][j] = 1
                if not (bit >> j) & 1 and X[i][j] == 1:
                    X[i][j] = 0
        if all(all(X[i][j] == Y[i][j] for j in range(N)) for i in range(N)):
            ans = max(ans, bin(bit).count("1"))
        for i in range(N):
            for j in range(N):
                if i == j:
                    continue
                X[i][j] = Y[i][j]
    print(ans)
