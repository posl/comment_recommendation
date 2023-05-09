def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    X = [0] * N
    # X[0] = (A[0] + A[1] - A[N-1]) / 2
    X[0] = (A[0] + A[1] - A[N-1]) // 2
    for i in range(1, N):
        X[i] = A[i-1] - X[i-1]
    print(*X)
