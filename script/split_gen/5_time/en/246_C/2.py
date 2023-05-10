def main():
    N, K, X = map(int, input().split())
    A = list(map(int, input().split()))
    total = 0
    for i in range(N):
        total += max(A[i] - K * X, 0)
    print(total)
