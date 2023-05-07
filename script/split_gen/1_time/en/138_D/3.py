def main():
    N, Q = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(N - 1)]
    operations = [list(map(int, input().split())) for _ in range(Q)]
    print(*solve(N, Q, edges, operations))
