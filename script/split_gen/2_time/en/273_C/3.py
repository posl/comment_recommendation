def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    B = sorted(A)
    C = [0] * (N + 1)
    for i in range(N):
        C[i + 1] = C[i] + B[i]
    for i in range(N):
        idx = B.index(A[i])
        print(N - idx - (C[N] - C[idx + 1]) + A[i])
main()
