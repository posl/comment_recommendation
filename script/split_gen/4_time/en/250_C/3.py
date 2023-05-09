def main():
    N, Q = map(int, input().split())
    X = [int(input()) for _ in range(Q)]
    A = [i for i in range(1, N+1)]
    for i in range(Q-1, -1, -1):
        A[i], A[i+1] = A[i+1], A[i]
        if A[i+1] == X[i]:
            A[i+1], A[i+2] = A[i+2], A[i+1]
    print(*A)
