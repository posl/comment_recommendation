def main():
    N, Q = map(int, input().split())
    X = [int(input()) for _ in range(Q)]
    Y = list(range(1,N+1))
    for x in X:
        idx = Y.index(x)
        Y[idx], Y[idx+1] = Y[idx+1], Y[idx]
    print(*Y)
