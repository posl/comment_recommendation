def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * (2 * N + 1)
    for i in range(N):
        B[A[i]] = i + 1
    C = [0] * (2 * N + 1)
    for i in range(2 * N, 0, -1):
        p = i
        while p <= 2 * N:
            C[p] += 1
            p += p & -p
        p = B[i]
        while p <= 2 * N:
            C[p] -= 1
            p += p & -p
    for i in range(1, 2 * N + 1):
        print(C[i])
main()
