def main():
    N, K = map(int, input().split())
    C = list(map(int, input().split()))
    print(solve(N, K, C))
