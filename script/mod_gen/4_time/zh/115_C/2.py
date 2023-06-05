def solve():
    N, K = map(int, input().split())
    h = [int(input()) for _ in range(N)]
    h.sort()
    print(h[K-1] - h[0])
solve()
