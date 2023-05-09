def solve():
    N, K = map(int, input().split())
    P = [list(map(int, input().split())) for _ in range(N)]
    P = [sum(p) for p in P]
    P.sort(reverse=True)
    print('Yes' if P[K-1] != P[K] else 'No')

if __name__ == '__main__':
    solve()