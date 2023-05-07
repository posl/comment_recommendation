def main():
    N, K = map(int, input().split())
    S = [input() for i in range(N)]
    print(solve(N, K, S))
