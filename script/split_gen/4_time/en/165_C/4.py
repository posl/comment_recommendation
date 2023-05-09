def main():
    N, M, Q = map(int, input().split())
    L = [list(map(int, input().split())) for _ in range(Q)]
    print(solve(N, M, Q, L))
