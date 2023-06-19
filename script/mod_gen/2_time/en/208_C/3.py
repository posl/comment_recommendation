def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = sorted(A)
    C = [0] * N
    for i in range(N):
        C[i] = B.index(A[i])
    D = [0] * N
    for i in range(N):
        D[C[i]] = i
    E = [0] * N
    for i in range(N):
        E[i] = (K - 1) // N
    F = (K - 1) % N
    for i in range(F):
        E[D[i]] += 1
    for i in range(N):
        print(E[i] + 1)
main()
