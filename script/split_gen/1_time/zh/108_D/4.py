def solve():
    L = int(input())
    N = L + 1
    M = 2 * L + 3
    print(N, M)
    for i in range(1, L + 1):
        print(i, i + 1, 0)
        print(i, i + 1, L - i)
    print(L + 1, N, 0)
    print(L + 1, N, 1)
    print(N - 1, N, 0)
solve()
