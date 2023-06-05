def main():
    # N = int(input())
    # A = list(map(int, input().split()))
    N = 7
    A = [1, 2, 3, 4, 5, 6]
    B = [0] * N
    for i in range(1, N):
        B[A[i] - 1] += 1
    for i in range(N):
        print(B[i])
