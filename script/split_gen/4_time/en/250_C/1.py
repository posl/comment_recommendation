def main():
    N, Q = map(int, input().split())
    A = list(range(1, N + 1))
    for _ in range(Q):
        x = int(input()) - 1
        A[x], A[x + 1] = A[x + 1], A[x]
    print(*A)
