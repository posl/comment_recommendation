def solve():
    N, A, X, Y = map(int, input().split())
    print(min(N, A) * X + max(0, N - A) * Y)

if __name__ == '__main__':
    solve()