def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    X = K
    for i in range(N):
        X = X & A[i]
    print(K * N + sum(A) - X * N)
