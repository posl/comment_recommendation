def main():
    N = int(input())
    A = list(map(int, input().split()))
    M = [0] * N
    M[0] = (A[0] + A[N - 1] - A[1]) // 2
    for i in range(1, N):
        M[i] = A[i - 1] - M[i - 1]
    print(*M)
