def main():
    N, Q = map(int, input().split())
    A = [i for i in range(1, N + 1)]
    for _ in range(Q):
        x = int(input())
        if x == N:
            A[0], A[N - 1] = A[N - 1], A[0]
        else:
            A[x], A[x - 1] = A[x - 1], A[x]
    print(*A)
