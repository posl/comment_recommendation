def main():
    # Get input here
    N, M, K = map(int, input().strip().split())
    AB = [tuple(map(int, input().strip().split())) for _ in range(M)]
    CD = [tuple(map(int, input().strip().split())) for _ in range(K)]
    # Get output here
    print(*solve(N, M, K, AB, CD))
