def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = [0] * N
    for i in range(N):
        C[i] = B[i] - A[i] + 1
    for i in range(1, N):
        C[i] *= C[i-1]
        C[i] %= 998244353
    print(C[N-1])
