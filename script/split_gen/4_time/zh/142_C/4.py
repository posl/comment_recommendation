def main():
    # N = int(input())
    # A = list(map(int, input().split()))
    N = 8
    A = [8, 2, 7, 3, 4, 5, 6, 1]
    B = [0] * N
    for i in range(N):
        B[A[i] - 1] = i + 1
    print(B)
