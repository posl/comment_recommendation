def f(A, B, K):
    if A == 0:
        return 'b' * B
    if B == 0:
        return 'a' * A
    if K <= C[A - 1][B]:
        return 'a' + f(A - 1, B, K)
    else:
        return 'b' + f(A, B - 1, K - C[A - 1][B])
A, B, K = map(int, input().split())
C = [[0] * (B + 1) for _ in range(A + 1)]
for i in range(A + 1):
    for j in range(B + 1):
        if i == 0 and j == 0:
            C[i][j] = 1
        elif i == 0:
            C[i][j] = C[i][j - 1]
        elif j == 0:
            C[i][j] = C[i - 1][j]
        else:
            C[i][j] = C[i - 1][j] + C[i][j - 1]
print(f(A, B, K))

if __name__ == '__main__':
    f()