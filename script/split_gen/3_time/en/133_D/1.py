def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * N
    for i in range(N):
        B[i] = A[i] - A[i - 1]
    C = [0] * N
    for i in range(N):
        C[i] = B[i] + B[(i + 1) % N]
    D = [0] * N
    for i in range(N):
        D[i] = C[i] // 2
    print(*D)
