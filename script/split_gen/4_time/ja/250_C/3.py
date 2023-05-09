def main():
    N, Q = map(int, input().split())
    X = [int(input()) for _ in range(Q)]
    A = [i for i in range(1, N+1)]
    for x in X:
        A[x-1], A[x] = A[x], A[x-1]
    print(*A)
