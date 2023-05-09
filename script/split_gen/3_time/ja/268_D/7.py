def main():
    N, M = map(int, input().split())
    S = [input() for _ in range(N)]
    T = [input() for _ in range(M)]
    X = ""
    for i in range(N):
        X += S[i]
        if i != N-1:
            X += "_"
    if X in T:
        print(-1)
    else:
        print(X)
