def main():
    N = int(input())
    A = list(map(int, input().split()))
    M = N * (N + 1) // 2
    B = [0] * M
    b = 0
    for i in range(N):
        for j in range(i, N):
            B[b] = A[j]
            b += 1
    B.sort()
    print(B[M // 2])
