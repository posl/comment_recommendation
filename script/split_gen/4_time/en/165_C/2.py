def main():
    N, M, Q = map(int, input().split())
    A = [0] * (N + 1)
    for i in range(Q):
        a, b, c, d = map(int, input().split())
        A[a - 1] += 1
        A[b] -= 1
    for i in range(N):
        A[i + 1] += A[i]
    print(sum(sorted(A[:N])[:M]))
