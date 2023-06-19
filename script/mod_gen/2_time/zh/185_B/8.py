def solve():
    N, M, T = map(int, input().split())
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    for i in range(M):
        if i == 0:
            N -= A[i]
        else:
            N -= A[i] - B[i - 1]
        if N <= 0:
            print("No")
            exit()
        N += B[i] - A[i]
        N = min(N, N)
    N -= T - B[M - 1]
    if N <= 0:
        print("No")
    else:
        print("Yes")

if __name__ == '__main__':
    solve()