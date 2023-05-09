def solve():
    N, L = map(int, input().split())
    print((N * (2 * L + N - 1)) // 2 - L * N)
solve()

if __name__ == '__main__':
    solve()