def solve():
    N, D = map(int, input().split())
    print((N + 2 * D) // (2 * D + 1))
solve()

if __name__ == '__main__':
    solve()