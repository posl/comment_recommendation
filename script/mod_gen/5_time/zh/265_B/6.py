def solve():
    N, M, T = map(int, input().split())
    A = list(map(int, input().split()))
    B = [0] * (N-1)
    for i in range(N-1):
        B[i] = A[i]
    X = [0] * M
    Y = [0] * M
    for i in range(M):
        X[i], Y[i] = map(int, input().split())
    for i in range(M):
        B[X[i]-2] += Y[i]
    for i in range(N-1):
        T -= B[i]
        if T <= 0:
            print('No')
            exit()
    print('Yes')

if __name__ == '__main__':
    solve()