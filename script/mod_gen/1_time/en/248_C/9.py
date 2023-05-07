def main():
    N, M, K = map(int, input().split())
    A = [1] * N
    for i in range(1, N):
        A[i] = A[i-1] * (M-1)
    for i in range(N-1, 0, -1):
        A[i] -= A[i-1] * (M-1)
    print(sum(A) % 998244353)

if __name__ == '__main__':
    main()