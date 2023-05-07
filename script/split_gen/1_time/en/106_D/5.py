def main():
    N, M, Q = map(int, input().split())
    train = [0] * (N + 1)
    for _ in range(M):
        L, R = map(int, input().split())
        train[L - 1] += 1
        train[R] -= 1
    for i in range(1, N + 1):
        train[i] = train[i - 1] + train[i]
    for _ in range(Q):
        p, q = map(int, input().split())
        print(train[q] - train[p - 1])
