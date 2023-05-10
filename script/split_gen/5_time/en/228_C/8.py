def main():
    N, K = map(int, input().split())
    P = [list(map(int, input().split())) for _ in range(N)]
    print('Yes' if sum([sum(p) >= K for p in P]) == N else 'No')
