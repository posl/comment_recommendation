def solve():
    N, K = map(int, input().split())
    print(N * (N + 1) * K * 100 // 2)
