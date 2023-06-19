def main():
    N, K, M = map(int, input().split())
    A = list(map(int, input().split()))
    X = M * N - sum(A)
    if X > K:
        print(-1)
    elif X < 0:
        print(0)
    else:
        print(X)
