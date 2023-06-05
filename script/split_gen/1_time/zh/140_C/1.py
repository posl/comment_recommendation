def main():
    N = int(input())
    B = list(map(int, input().split()))
    A = [0] * N
    for i in range(N - 1):
        A[i] = max(B[i], B[i + 1])
    A[N - 1] = B[N - 2]
    print(sum(A))
