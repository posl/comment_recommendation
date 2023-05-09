def main():
    N = int(input())
    edges = [list(map(int, input().split())) for _ in range(N - 1)]
    print(solve(N, edges))
