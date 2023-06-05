def check_honesty(N, A, x, y):
    honest = [0] * N
    for i in range(0, N):
        if (A[i] == 0):
            honest[i] = 1
            continue
        for j in range(0, A[i]):
            if (y[i][j] == 1):
                honest[x[i][j] - 1] = 1
    return sum(honest)
N = int(input())
A = [0] * N
x = [0] * N
y = [0] * N
for i in range(0, N):
    A[i] = int(input())
    x[i] = [0] * A[i]
    y[i] = [0] * A[i]
    for j in range(0, A[i]):
        x[i][j], y[i][j] = map(int, input().split())
print(check_honesty(N, A, x, y))
