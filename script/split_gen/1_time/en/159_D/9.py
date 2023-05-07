def main():
    N = int(input())
    A = [int(a) for a in input().split()]
    A = [0] + A
    B = [0] * (N + 1)
    for i in range(1, N + 1):
        B[A[i]] += 1
    C = [0] * (N + 1)
    for i in range(1, N + 1):
        C[i] = B[i] * (B[i] - 1) // 2
    for i in range(1, N + 1):
        print(sum(C) - C[A[i]] + (B[A[i]] - 1) * (B[A[i]] - 2) // 2)
