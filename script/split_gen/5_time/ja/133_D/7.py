def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * N
    for i in range(N):
        if i % 2 == 0:
            B[0] += A[i]
        else:
            B[0] -= A[i]
    for i in range(1, N):
        B[i] = (A[i-1] - B[i-1] // 2) * 2
    print(' '.join(map(str, B)))
