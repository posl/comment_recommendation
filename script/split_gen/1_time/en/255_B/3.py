def main():
    import math
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    X = [0] * N
    Y = [0] * N
    for i in range(N):
        X[i], Y[i] = map(int, input().split())
    ans = 0
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            ans = max(ans, math.sqrt((X[i] - X[j]) ** 2 + (Y[i] - Y[j]) ** 2))
    for i in range(K - 1):
        ans = max(ans, math.sqrt((X[A[i] - 1] - X[A[i + 1] - 1]) ** 2 + (Y[A[i] - 1] - Y[A[i + 1] - 1]) ** 2))
    print(ans / 2)
