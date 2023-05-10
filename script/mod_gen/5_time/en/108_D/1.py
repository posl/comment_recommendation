def solve():
    L = int(input())
    N = 1
    while 2 ** N <= L:
        N += 1
    M = N * (N - 1) // 2
    print(N, M)
    for i in range(1, N):
        print(i, i + 1, 0)
    for i in range(1, N):
        for j in range(i + 2, N + 1):
            print(i, j, 2 ** (i - 1))
solve()

if __name__ == '__main__':
    solve()