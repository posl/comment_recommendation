def solve():
    N, K = map(int, input().split())
    print(N * (N + 1) * K * 100 // 2)

if __name__ == '__main__':
    solve()