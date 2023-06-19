def solve(L):
    N = 20
    M = 60
    print(N, M)
    for i in range(N - 1):
        print(i + 1, i + 2, 0)
    for i in range(M - N + 1):
        print(i + 1, i + N, i % L + 1)

if __name__ == '__main__':
    solve()